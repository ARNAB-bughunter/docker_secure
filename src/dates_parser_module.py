import re
from src.date_regex import all_regex
import requests
from ast import literal_eval 


SPLITED_DATE_REGEX = r"/|\.|-| "

def sanity_year_check(dates,format_):
    final_result = []
    for date_ in dates:
        splited_date = re.split(SPLITED_DATE_REGEX, date_['text'])
        splited_format = re.split(SPLITED_DATE_REGEX, format_)
        if len(splited_date) == 2 and len(splited_format) == 2 and all([True if format_symbol not in ['%d','%y'] else False for format_symbol in splited_format ]):
            year_ = splited_date[0] if len(splited_date[0]) == 4 and splited_date[0].isdigit()  else splited_date[1]
            if year_.startswith("20") and  2000 <= int(year_) <= 2050 :
                final_result.append(date_)
        else:
            final_result.append(date_)
    if len(final_result) == 0:
        return []
    return final_result


def sanity_month_check(dates,format_):
    final_result = []
    try:
        for date_ in dates:
            splited_date = re.split(SPLITED_DATE_REGEX, date_['text'])
            splited_format = re.split(SPLITED_DATE_REGEX, format_)


            if len(splited_date) ==  len(splited_format) and '%m' in splited_format:
                month_index = (splited_format.index("%m"))
                month_value = splited_date[month_index]
                if 1 <= int(month_value) <= 12:
                    final_result.append(date_)
            else:
                final_result.append(date_)
        
        if len(final_result) == 0:
            return []
    except Exception:
        pass
    return final_result


def sanity_day_check(dates,format_):
    final_result = []
    try:
        for date_ in dates:
            splited_date = re.split(SPLITED_DATE_REGEX, date_['text'])
            splited_format = re.split(SPLITED_DATE_REGEX, format_)


            if len(splited_date) ==  len(splited_format) and '%d' in splited_format:
                month_index = (splited_format.index("%d"))
                month_value = splited_date[month_index]
                if 1 <= int(month_value) <= 31:
                    final_result.append(date_)
            else:
                final_result.append(date_)
        
        if len(final_result) == 0:
            return []
    except Exception:
        pass
    
    return final_result

def sanity_swap(dates,format_):
    final_result = []
    try:
        for date_ in dates:
            splited_date = re.split(SPLITED_DATE_REGEX, date_['text'])
            splited_format = re.split(SPLITED_DATE_REGEX, format_)
            if len(splited_date) ==  len(splited_format) and '%m' in splited_format and '%d' in splited_format:
                map_ = {j: i for i, j in zip(splited_date, splited_format)}
                if not (1 <= int(map_['%m']) <= 12) and (1 <= int(map_['%d']) <= 31):
                    map_['%m'], map_['%d'] = map_['%d'], map_['%m']
                    differentiator_ = re.findall(SPLITED_DATE_REGEX, date_['text'])
                    new_text = differentiator_[0].join((map_.values()))
                    temp = {'label': 'DATE','text':new_text, "original_text":date_['original_text']}
                    final_result.append(temp)
                else:
                    final_result.append(date_)    
            else:
                final_result.append(date_)
    except Exception:
        pass
    return final_result


def make_output(flag, date_list, label, format):
    final_result = []
    for date in date_list:
        if isinstance(date, str):
            final_date = ""
            if '/' in date or '-' in date or '.' in date:
                final_date = re.sub(r"\s+", "", date)
            else:
                final_date = date
            # final_date = re.sub(r"th|st|nd|rd", "", final_date) final_date = " ".join([ re.sub(r"th|st|rd","",
            # date_part) if date_part.isalnum() and not date_part.isalpha() and not date_part.isdigit()  else
            # date_part for date_part in final_date.split()])
            if "september" not in final_date and "sept" in final_date:
                final_date = final_date.replace("sept", "sep")
            final_result.append({"label": label, "text": final_date, "original_text": final_date})
        elif isinstance(date, tuple):
            if '/' in date[0] or '-' in date[0] or '.' in date[0]:
                final_date = re.sub(r"\s+", "", date[0])
            else:
                final_date = date[0]
            # final_date = re.sub(r"th|st|nd|rd", "", final_date) final_date = " ".join([ re.sub(r"th|st|rd","",
            # date_part) if date_part.isalnum() and not date_part.isalpha() and not date_part.isdigit()  else
            # date_part for date_part in final_date.split()])
            if "september" not in final_date and "sept" in final_date:
                final_date = final_date.replace("sept", "sep")
            final_result.append({"label": label, "text": final_date, "original_text": final_date})
    return flag, final_result, format

def remove_mystopwords_from_datestring(sentence, corpus_info):
    my_stopwords = corpus_info["date_stopwords_corpus"]
    text_tokens = sentence.split(" ")
    tokens_filtered = [word for word in text_tokens if word not in my_stopwords]
    return " ".join(tokens_filtered)

def format_date(model_op):
    model_op = literal_eval(model_op)
    print("###",model_op)
    date_list = []
    for i in model_op['ner']:
        if i['label'] == 'DATE':
            date = i['text']
            date = date.replace('-','/').replace('.','/')
            date_list.append(date)
    return date_list


def check_is_range(inp_datetime):
    inp_datetime = inp_datetime.lower()
    months_list = re.findall(r'january|february|march|april|may|june|july|august|september|october|november|december|jan|feb|mar|apr|jun|jul|aug|sep|sept|oct|nov|dec',inp_datetime, re.I)
    break_point_list = re.findall(r'to|from|-',inp_datetime,re.I)

    if len(months_list) >= 2 and len(break_point_list):
        return True,months_list,break_point_list
    return False,[],[]

def parse_datetime(inp_datetime, corpus_info, doc_type, custom_ner_flag_not_required):
    try:
        inp_datetime = inp_datetime.replace(",", " ").replace("'"," ")
        inp_datetime = remove_mystopwords_from_datestring(inp_datetime, corpus_info)
        inp_datetime = " ".join([ re.sub(r"th|st|rd|nd","",word) if word.isalnum() and not word.isalpha() and not word.isdigit()  else word for word in inp_datetime.split()])

        is_range,month_list,break_point_list = check_is_range(inp_datetime)

        if doc_type == 'FST' or doc_type == None:
            all_regex_ = all_regex
        elif doc_type == 'INV':
            all_regex_ = all_regex
        elif doc_type == 'PO':
            all_regex_ = all_regex

        if is_range:
            for regex in all_regex_:
                inp_datetime = inp_datetime.lower()
                inp_datetime = re.sub(r"\d{1,2}:\d{1,2}:\d{1,2}", "", inp_datetime)
                inp_datetime = re.sub(r"\d{1,2}:\d{1,2}", "", inp_datetime)
                date_list = re.findall(regex[1], inp_datetime, re.I)
                if len(date_list) >= 2:
                    make_op = make_output(True, date_list,"DATE",regex[0])
                    if make_op[0]:
                        updated_dt_list = sanity_swap(make_op[1],make_op[2])
                        updated_dt_list = sanity_year_check(updated_dt_list, make_op[2])
                        updated_dt_list = sanity_month_check(updated_dt_list, make_op[2])
                        updated_dt_list = sanity_day_check(updated_dt_list, make_op[2])
                        if len(updated_dt_list) == 0:
                            return False, updated_dt_list, ""
                        return make_op[0], updated_dt_list, make_op[2]
                
            splited_inp_datetime = inp_datetime.split(break_point_list[0])
            if splited_inp_datetime:
                make_op = make_output(True, splited_inp_datetime, "DATE", "")
                if make_op[0]:
                    return make_op[0], make_op[1], make_op[2]
                
        else:
            for regex in all_regex_:
                inp_datetime = inp_datetime.lower()
                inp_datetime = re.sub(r"\d{1,2}:\d{1,2}:\d{1,2}", "", inp_datetime)
                inp_datetime = re.sub(r"\d{1,2}:\d{1,2}", "", inp_datetime)
                date_list = re.findall(regex[1], inp_datetime, re.I)
                if date_list:
                    make_op = make_output(True, date_list, "DATE", regex[0])
                    if make_op[0]:
                        updated_dt_list = sanity_swap(make_op[1],make_op[2])
                        updated_dt_list = sanity_year_check(updated_dt_list, make_op[2])
                        updated_dt_list = sanity_month_check(updated_dt_list, make_op[2])
                        updated_dt_list = sanity_day_check(updated_dt_list, make_op[2])
                        if len(updated_dt_list) == 0:
                            return False, updated_dt_list, ""
                        return make_op[0], updated_dt_list, make_op[2]
    except Exception:
        pass
    return False, [], ''