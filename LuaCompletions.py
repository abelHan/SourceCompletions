import sublime
import sublime_plugin

class ExampleCommand(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
        if not (view.match_selector(locations[0],'source.lua -string -comment -constant') or
               not view.match_selector(locations[0],'source.py -string -comment -constant')):
            return []

        return (
        	[
        		["hello\thello world","hello world"],
        		["nihao\tnihao shijie","nihao shijie"]
        	],sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS)

