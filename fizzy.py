#!/usr/bin/env python

# TODO: argparse, read from stdin

from sys import argv, exit
from textx.metamodel import metamodel_from_file
if len(argv) < 2:
  print("need file")
  exit()

mm = metamodel_from_file("fizzy.tx")
program = mm.model_from_file(argv[1])

if len(program.range) == 0:
  gen_range = [1, 100]
elif len(program.range) == 1:
  gen_range = [1, program.range[0]]
else:
  gen_range = program.range

if len(program.rules) == 0:
  class RuleFake():
    def __init__(self, triggers, string):
      self.triggers = triggers
      self.string = string
  rules = [RuleFake(triggers=[3], string="fizz"), RuleFake(triggers=[5], string="buzz")]
else:
  rules = program.rules

# now figure out direction and either add one or subtract one
if gen_range[0] > gen_range[1]:
  step = -1
else:
  step = 1

iteration_range = range(gen_range[0], gen_range[1] + step, step)

class RuleMatch():
  def __init__(self, rule_id, value, string):
    self.rule_id = rule_id
    self.value = value
    self.string = string

for i in iteration_range:
  triggered_rules = []
  for rule_id, rule in enumerate(rules):
    for trigger in rule.triggers:
      if i % trigger == 0:
        triggered_rules.append(RuleMatch(rule_id, trigger, rule.string))

  if len(triggered_rules) == 0:
    print(i)
  else:
    s = ""
    rules_in_string = set()

    # sort by rule_id and then value to achieve sorting by
    # value with ties broken by rule_id
    triggered_rules.sort(key=lambda e: e.rule_id)
    triggered_rules.sort(key=lambda e: e.value)

    for match in triggered_rules:
      if not match.rule_id in rules_in_string:
        rules_in_string.add(match.rule_id)
        s += match.string
    print(s)
