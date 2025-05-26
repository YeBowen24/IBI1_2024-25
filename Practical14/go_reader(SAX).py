import xml.sax  
from datetime import datetime  

# Define a SAX handler class for processing GO terms
class GOTermHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_data = ""
        self.current_term = {"id": "","namespace": "","is_a_count": 0}# Initialize the dictionary
        self.max_terms = {"molecular_function": {"id": [], "count": 0},"biological_process": {"id": [], "count": 0},"cellular_component": {"id": [], "count": 0}} #Initialize the max_terms dictionary, used to store information about the term with the most is_a elements in each namespace
        self.in_def = False

    def startElement(self, tag, attributes): # Handle the start tag in the XML document
        self.current_data = tag # Record the current tag being processed
        if tag == "term": # If a <term> tag is encountered, reset the current_term dictionary
            self.current_term = {"id": "","namespace": "","is_a_count": 0}
        elif tag == "is_a": # If an <is_a> tag is encountered, increment the is_a element count
            self.current_term["is_a_count"] += 1

    def endElement(self, tag): # Handle the end tag in the XML document
        if tag == "term": # If the end tag is <term>, then get the namespace, id, and is_a element count of the current term
            namespace = self.current_term["namespace"]
            term_id = self.current_term["id"]
            count = self.current_term["is_a_count"]
            if namespace in self.max_terms: # If the namespace is in the max_terms dictionary
                if count > self.max_terms[namespace]["count"]: # If the current term's is_a element count is bigger than the count recorded in max_terms
                    self.max_terms[namespace] = {"id": [term_id], "count": count} # Update the term id list and count for that namespace in max_terms
                elif count == self.max_terms[namespace]["count"]: # If the current term's is_a element count is equal to the count recorded in max_terms
                    self.max_terms[namespace]["id"].append(term_id) # Add the current term id to the term id list for that namespace in max_terms
        self.current_data = "" # Reset current_data to an empty string

    def characters(self, content): # Handle the end tag in the XML document
        if self.current_data == "id":
            self.current_term["id"] = content
        elif self.current_data == "namespace":
            self.current_term["namespace"] = content

def parse_xml_sax(file_path): # Parse an XML file using the SAX API
    start_time = datetime.now()  # Record the start time of function execution
    handler = GOTermHandler()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse(file_path) # Use the parser to parse the XML file at the specified path
    end_time = datetime.now()  # Record the end time of function execution
    elapsed_time = (end_time - start_time).total_seconds() # Calculate the total execution time of the function
    return handler.max_terms, elapsed_time # Return the most is_a elements and the execution time

sax_max_terms, sax_time = parse_xml_sax('go_obo.xml')

print("SAX API Results:")
for namespace, term in sax_max_terms.items(): # Iterate through each namespace and its corresponding term information in the max_terms dictionary
    print(f"Namespace: {namespace}")
    print("Term ID with most is_a elements:", ", ".join(term["id"]) if term["id"] else "None")
    print(f"Number of is_a elements: {term['count']}\n")
print(f"SAX API took {sax_time:.2f} seconds")