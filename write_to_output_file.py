# Write result to an output file
def write_results_to_file(tag_counts, port_proto_comb_counts, output_filename='output.txt'):
    # Open the output file with write mode
    with open(output_filename, mode='w') as file:
        # Write count of matches for each tag to the output file
        file.write("Count of matches for each tag, sample o/p shown below\n\n")
        file.write("Tag Counts:\n\n")
        file.write("Tag, Count\n")
        for tag, count in tag_counts.items():
            file.write(f"{tag}, {count}\n")
        file.write("\n")
        # Write count of matches for each port/protocol combination to the output file
        file.write("Count of matches for each port/protocol combination\n\n")
        file.write("Port/Protocol Combination Counts:\n\n")
        file.write("Port,Protocol,Count\n")
        for comb, count in port_proto_comb_counts.items():
            dstport, protocol = comb
            file.write(f"{dstport}, {protocol}, {count}\n")