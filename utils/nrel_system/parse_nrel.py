import utils.nrel_system.parse_nrel_csv as parse_nrel_csv
import utils.nrel_system.parse_nrel_data as parse_nrel_data

def merge_nrel(nrel_filename_list):
    parsed_nrel_list = []
    for nrel_filename in nrel_filename_list:
        parsed_nrel_list.append(parse_nrel_csv.main(nrel_filename))
    nrel, L = parse_nrel_data.main(parsed_nrel_list)
    return nrel, L

def main(nrel_filename_list):
    return merge_nrel(nrel_filename_list)