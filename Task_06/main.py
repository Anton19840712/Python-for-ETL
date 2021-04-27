from charsreader import*
from charswriter import*
from datacooker import*
from filereader import*
from filewriter import*
from repositorymanager import*
from wordsreader import*
from wordwriter import*

# Main area
def main():
    pass
if __name__ == "__main__":
    # path to store files to process to smoke test should be here 
    # 'D:\\proc\\testdir' by default.
    #directory = RepositoryManager().define_directory()
    
    # Extraction area
    file_names = RepositoryManager.gain_me_file_names() 
    path_names = RepositoryManager.gain_me_path_list(file_names)
    data_pool = FileReader.read_files_data(path_names)  
    # Transformation area
    transfomed_data = DataCooker.cook_me_data(data_pool)
    counted_chars_list = CharsReader.count_chars_pool(transfomed_data)
    cleaned_from_whitespaces =  DataCooker.cut_whitesapces(counted_chars_list)
    counted_upper = DataCooker.count_upper_chars(cleaned_from_whitespaces)
    sorted_ingredients = DataCooker.sort_me_list(cleaned_from_whitespaces)
    sum_of_values = DataCooker.count_sum_of_values(sorted_ingredients)
    #words processing
    lowered_case_string = DataCooker.lower_case_me_string(transfomed_data)
    counted_words_list = WordsReader.word_count(lowered_case_string)
    sorted_value_list = DataCooker.sort_me_list(counted_words_list)
    # Loading area
    CharsWriter.write_me_chars(sorted_ingredients, sum_of_values, counted_upper)
    WordWriter.write_me_words(sorted_value_list)
    main()

       

     
