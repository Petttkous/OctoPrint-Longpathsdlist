# coding=utf-8

import octoprint.plugin
import logging

class LongPathSDListPlugin(octoprint.plugin.OctoPrintPlugin):
    def on_sd_list(self, comm, line, *args, **kwargs):
        if "End file list" not in line:
            return line

        for file in comm._sdFiles:
            shortFile = file[0]
            # logging.getLogger("octoprint.plugin." + __name__).info("Sending: {f}.".format(f = "M33 " + shortFile))
            comm._enqueue_for_sending("M33 " + shortFile)
        return line

__plugin_pythoncompat__ = ">=2.7,<4"
def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = LongPathSDListPlugin()

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.comm.protocol.gcode.received": __plugin_implementation__.on_sd_list
    }