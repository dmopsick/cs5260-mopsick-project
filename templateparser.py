from template import Template
from myresource import MyResource, DEFAULT_RESOURCE_WEIGHT

##########################
# Parse text file into a list of templates
#
#
#########################
def parse_template(file_path):
    template_obj_list = []

    with open(file_path, 'r') as file:
        content = file.read()

        # Split the templates | They are split by two spaces
        templates = content.split('\n\n')

        # print(templates[0])

        # Build each template
        for template in templates:
            inputs =[]
            outputs =[]

            # Remove the parentheses from the text for parsing
            template = template.replace("(", "")
            template = template.replace(")", "")

            # Split the template by lines
            template_lines = template.split("\n")

            # Name is the first line of each template
            name = template_lines[0]

            # Logging for testing
            print("Parsing template: " + name)

            # Type is the second line
            template_type = template_lines[1]

            print("Template is type: " + template_type)

            # First line is the first input
            first_input_line = template_lines[2]

            # Trim the first input line
            first_input_line = first_input_line.replace("INPUTS", "").strip()

            # Split the input line by space
            first_input_resource_raw = first_input_line.split(" ")
            
            # Load the first input resource
            first_input_resource_obj = MyResource(first_input_resource_raw[0], first_input_resource_raw[1], DEFAULT_RESOURCE_WEIGHT)
            
            # Logging for testing
            print("Adding INPUT - Name: " + first_input_resource_obj.NAME + " Quantity: " + first_input_resource_obj.QUANTITY)

            # Add the resource to the input list
            inputs.append(first_input_resource_obj)

            # Track where in the array of lines we are
            current_index = 3

            # Build the rest of the inputs
            while ("OUTPUTS" not in template_lines[current_index]):
                # Build each object
                input_resource_raw = template_lines[current_index].strip().split(" ")

                input_resource_obj = MyResource(input_resource_raw[0], input_resource_raw[1], DEFAULT_RESOURCE_WEIGHT)

                # Add the created object to the list of inputs
                inputs.append(input_resource_obj)

                # print("Adding INPUT - Name: " + input_resource_obj.NAME + " Quantity: " + input_resource_obj.QUANTITY)

                # Advance to the next line
                current_index += 1
            
            # Time to parse the outputs
            first_output_line = template_lines[current_index].replace("OUTPUTS", "").strip()

            first_output_resource_raw = first_output_line.split(" ")

            # Build the output template object
            first_output_resource_obj = MyResource(first_output_resource_raw[0], first_input_resource_raw[1], DEFAULT_RESOURCE_WEIGHT)

            print("Adding OUTPUT - Name: " + first_output_resource_obj.NAME + " Quantity: " + first_output_resource_obj.QUANTITY)

            # Build out the list
            outputs.append(first_input_resource_obj)

            current_index += 1

            # Parse the rest of the outputs
            while (current_index < len(template_lines)):
                # Build each object
                output_resource_raw = template_lines[current_index].strip().split(" ")

                if len(output_resource_raw) < 2:
                    current_index += 1
                    continue

                # print(template_lines[current_index])

                # Split the name from the quantity
                output_resource_obj = MyResource(output_resource_raw[0], output_resource_raw[1], DEFAULT_RESOURCE_WEIGHT)
                print("Adding OUTPUT - Name: " + output_resource_raw[0] + " Quantity: " + output_resource_raw[1])

                outputs.append(output_resource_obj)

                current_index += 1
            
            # Time to finally create the template
            template = Template(name, template_type, inputs, outputs)

            print("Created Template: " + template.NAME + " with " + str(len(inputs)) + " inputs and " + str(len(outputs)) + " outputs")

            # Add the created template to the list of templates
            template_obj_list.append(template)

        return template_obj_list

        