import copy

from action import Action

def parse_template(file_path, in_resources):
    resources = copy.deepcopy(in_resources)
    type = 'TRANSFORM'
    actions = []
    with open(file_path, 'r') as file:
      content = file.read()
      templates = content.split("\n\n")  # Assuming each template is separated by two newlines
      for template in templates:
        inputs = []
        outputs = []
        name = template.split("\n")[0] # Assuming template name is alone on first line
        template = template.replace(name, "")
        template = template.replace("\n", "")
        template = template.replace("TRANSFORMC", "")
        halves = template.split("))(")
        ins = halves[0].replace("((INPUTS(", "").split(")(")
        outs = halves[1].replace("OUTPUTS(", "")
        outs = outs.replace(")))", "").split(")(")

        for resource in resources:
          for input in ins:
            if resource.NAME in input:
              input = input.replace(resource.NAME, "")
              resource.QUANTITY = int(input)
              inputs.append(resource)
          for output in outs:
            if resource.NAME in output:
              if not 'Waste' in output or ('Waste' in output and 'Waste' in resource.NAME):
                output = output.replace(resource.NAME, "")
                resource.QUANTITY = int(output)
                outputs.append(resource)
        
        actions.append(Action(name, type, inputs, outputs))
    # Add the TRANSFER action template.
    actions.append(Action("TransferTemplate", "TRANSFER"))
    return actions

