import logging
import subprocess
import pwnagotchi
import pwnagotchi.plugins as plugins
import pwnagotchi.ui.fonts as fonts

from pwnagotchi.ui.components import LabeledValue
from pwnagotchi.ui.view import BLACK


class Dashboard(plugins.Plugin):
    __author__ = 'doki'
    __version__ = '1.0.1'
    __license__ = 'GPL3'
    __description__ = 'Dashboard plugin showing deauths, handshakes, memory, temp, CPU load, and cracked handshake count.'

    def __init__(self):
        self.deauth_counter = 0
        self.handshake_counter = 0

    def on_loaded(self):
        logging.info("[Dashboard]: plugin loaded.")

    def mem_usage(self):
        return int(pwnagotchi.mem_usage() * 100)

    def cpu_load(self):
        return int(pwnagotchi.cpu_load() * 100)

    def cpu_temp(self):
        return int(pwnagotchi.temperature())

    def get_cracked_count(self):
        try:
            result = subprocess.check_output(
                "uniq -i /root/handshakes/wpa-sec.cracked.potfile | wc -l",
                shell=True
            )
            return result.decode().strip()
        except Exception as e:
            logging.error("[Dashboard]: Failed to get cracked count: %s", e)
            return "0"

    def on_ui_setup(self, ui):
        def pos(key): return int(self.options[key])

        ui.add_element('ram', LabeledValue(
            color=BLACK, label='', value='mem',
            position=(pos("mem_x_pos"), pos("mem_y_pos")),
            label_font=fonts.Small, text_font=fonts.Bold))

        ui.add_element('cpu', LabeledValue(
            color=BLACK, label='', value='cpu',
            position=(pos("cpu_x_pos"), pos("cpu_y_pos")),
            label_font=fonts.Small, text_font=fonts.Bold))

        ui.add_element('tmp', LabeledValue(
            color=BLACK, label='', value='tmp',
            position=(pos("tmp_x_pos"), pos("tmp_y_pos")),
            label_font=fonts.Small, text_font=fonts.Bold))

        ui.add_element('deauth', LabeledValue(
            color=BLACK, label='', value=str(self.deauth_counter),
            position=(pos("deauth_x_pos"), pos("deauth_y_pos")),
            label_font=fonts.Bold, text_font=fonts.Bold))

        ui.add_element('hand', LabeledValue(
            color=BLACK, label='', value=str(self.handshake_counter),
            position=(pos("hand_x_pos"), pos("hand_y_pos")),
            label_font=fonts.Bold, text_font=fonts.Bold))

        ui.add_element('cracked', LabeledValue(
            color=BLACK, label='', value='',
            position=(pos("cracked_x_pos"), pos("cracked_y_pos")),
            label_font=fonts.Bold, text_font=fonts.Bold))

    def on_unload(self, ui):
        with ui._lock:
            for key in ['ram', 'cpu', 'tmp', 'deauth', 'hand', 'cracked']:
                ui.remove_element(key)

    def on_ui_update(self, ui):
        ui.set('cracked', self.get_cracked_count())
        ui.set('ram', f"{self.mem_usage()}%")
        ui.set('cpu', f"{self.cpu_load()}%")
        ui.set('tmp', f"{self.cpu_temp()}°C")
        ui.set('deauth', str(self.deauth_counter))
        ui.set('hand', str(self.handshake_counter))

    def on_deauthentication(self, agent, access_point, client_station):
        self.deauth_counter += 1

    def on_handshake(self, agent, filename, access_point, client_station):
        self.handshake_counter += 1
