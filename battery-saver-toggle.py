#!/usr/bin/env python3

import os
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk, AppIndicator3

CONSERVATION_PATH = "/sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode"

class ConservationIndicator:
    def __init__(self):
        self.app = 'conservation-mode-toggle'
        icon = self.get_icon()
        self.indicator = AppIndicator3.Indicator.new(
            self.app, icon,
            AppIndicator3.IndicatorCategory.APPLICATION_STATUS
        )
        self.indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
        self.indicator.set_menu(self.build_menu())
        self.indicator.set_icon_full(self.get_icon(), "battery-good")

    def get_icon(self):
        status = self.get_status()
        return "battery-good" if status else "battery-empty"

    def get_status(self):
        try:
            with open(CONSERVATION_PATH, 'r') as f:
                return f.read().strip() == '1'
        except:
            return False

    def toggle_status(self, _):
        new_value = '0' if self.get_status() else '1'
        os.system(f"echo {new_value} | pkexec tee {CONSERVATION_PATH}")
        self.indicator.set_icon_full(self.get_icon(), "battery-good")
        self.update_menu()

    def build_menu(self):
        menu = Gtk.Menu()

        self.status_item = Gtk.MenuItem(label=self.get_tooltip())
        self.status_item.set_sensitive(False)
        self.status_item.show()
        menu.append(self.status_item)

        toggle_item = Gtk.MenuItem(label="Switch mode")
        toggle_item.connect("activate", self.toggle_status)
        toggle_item.show()
        menu.append(toggle_item)

        quit_item = Gtk.MenuItem(label="Quit")
        quit_item.connect("activate", self.quit)
        quit_item.show()
        menu.append(quit_item)

        return menu

    def quit(self, _):
        Gtk.main_quit()

    def get_tooltip(self):
        if self.get_status():
            return "Battery saver mode is ON"
        else:
            return "Battery saver mode is OFF"

    def update_menu(self):
        self.status_item.set_label(self.get_tooltip())

    def run(self):
        Gtk.main()

if __name__ == "__main__":
    app = ConservationIndicator()
    app.run()

