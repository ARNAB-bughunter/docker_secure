all_regex = [
        

        ["%d/%m/%Y",r"(\d{1,2}\s*/\s*\d{1,2}\s*/\s*\d{4})"], # dd/mm/yyyy
        ["%d/%m/%y",r"(\d{1,2}\s*/\s*\d{1,2}\s*/\s*\d{2})"], # dd/mm/yy
        ["%d-%m-%Y",r"(\d{1,2}\s*-\s*\d{1,2}\s*-\s*\d{4})"], # dd-mm-yyyy
        ["%d-%m-%y",r"(\d{1,2}\s*-\s*\d{1,2}\s*-\s*\d{2})"], # dd-mm-yy
        ["%d.%m.%Y",r"(\d{1,2}\s*\.\s*\d{1,2}\s*\.\s*\d{4})"], # dd.mm.yyyy
        ["%d.%m.%y",r"(\d{1,2}\s*\.\s*\d{1,2}\s*\.\s*\d{2})"], # dd.mm.yy
        ["%d %m %Y",r"(\d{1,2}\s+\d{1,2}\s+\d{4})"], # dd mm yyyy
        ["%d %m %y",r"(\d{1,2}\s+\d{1,2}\s+\d{2})"], # dd mm yy


        ["%d %B %Y",r"(\d{1,2}(th|st|nd|rd)\s+(january|february|march|april|may|june|july|august|september|october|november|december)\s+\d{4})"], #dd(th|st|nd|rd) month yyyy
        ["%d %B %y",r"(\d{1,2}(th|st|nd|rd)\s+(january|february|march|april|may|june|july|august|september|october|november|december)\s+\d{2})"], #dd(th|st|nd|rd) month yy
        ["%d %b %Y",r"(\d{1,2}(th|st|nd|rd)\s+(jan|feb|mar|apr|jun|jul|aug|sep|sept|oct|nov|dec)\s+\d{4})"], #dd(th|st|nd|rd) month yyyy
        ["%d %b %y",r"(\d{1,2}(th|st|nd|rd)\s+(jan|feb|mar|apr|jun|jul|aug|sep|sept|oct|nov|dec)\s+\d{2})"], #dd(th|st|nd|rd) month yy


        ["%d/%B/%Y",r"(\d{1,2}\s*/\s*(january|february|march|april|may|june|july|august|september|october|november|december)\s*/\s*\d{4})"], # dd/month/yyyy
        ["%d/%B/%y",r"(\d{1,2}\s*/\s*(january|february|march|april|may|june|july|august|september|october|november|december)\s*/\s*\d{2})"], # dd/month/yyyy
        ["%d/%b/%Y",r"(\d{1,2}\s*/\s*(jan|feb|mar|apr|jun|jul|aug|sep|sept|oct|nov|dec)\s*/\s*\d{4})"], # dd/month/yyyy
        ["%d/%b/%y",r"(\d{1,2}\s*/\s*(jan|feb|mar|apr|jun|jul|aug|sep|sept|oct|nov|dec)\s*/\s*\d{2})"], # dd/month/yy

        ["%d-%B-%Y",r"(\d{1,2}\s*-\s*(january|february|march|april|may|june|july|august|september|october|november|december)\s*-\s*\d{4})"], # dd-month-yyyy
        ["%d-%B-%y",r"(\d{1,2}\s*-\s*(january|february|march|april|may|june|july|august|september|october|november|december)\s*-\s*\d{2})"], # dd-month-yy
        ["%d-%b-%Y",r"(\d{1,2}\s*-\s*(jan|feb|mar|apr|jun|jul|aug|sep|sept|oct|nov|dec)\s*-\s*\d{4})"], # dd-month-yyyy
        ["%d-%b-%y",r"(\d{1,2}\s*-\s*(jan|feb|mar|apr|jun|jul|aug|sep|sept|oct|nov|dec)\s*-\s*\d{2})"], # dd-month-yy

        ["%d.%B.%Y",r"(\d{1,2}\s*\.\s*(january|february|march|april|may|june|july|august|september|october|november|december)\s*\.\s*\d{4})"], # dd.month.yyyy
        ["%d.%B.%y",r"(\d{1,2}\s*\.\s*(january|february|march|april|may|june|july|august|september|october|november|december)\s*\.\s*\d{2})"], # dd.month.yy
        ["%d.%b.%Y",r"(\d{1,2}\s*\.\s*(jan|feb|mar|apr|jun|jul|aug|sep|sept|oct|nov|dec)\s*\.\s*\d{4})"], # dd.month.yyyy
        ["%d.%b.%y",r"(\d{1,2}\s*\.\s*(jan|feb|mar|apr|jun|jul|aug|sep|sept|oct|nov|dec)\s*\.\s*\d{2})"], # dd.month.yy
        ["%d %B %Y",r"(\d{1,2}\s+(january|february|march|april|may|june|july|august|september|october|november|december)\s+\d{4})"], # dd month yyyy
        ["%d %B %y",r"(\d{1,2}\s+(january|february|march|april|may|june|july|august|september|october|november|december)\s+\d{2})"], # dd month yy
        ["%d %b %Y",r"(\d{1,2}\s+(jan|feb|mar|apr|jun|jul|aug|sep|sept|oct|nov|dec)\s+\d{4})"], # dd month yyyy
        ["%d %b %y",r"(\d{1,2}\s+(jan|feb|mar|apr|jun|jul|aug|sep|sept|oct|nov|dec)\s+\d{2})"], # dd month yy


        ["%B/%d/%Y",r"((january|february|march|april|may|june|july|august|september|october|november|december)\s*/\s*\d{1,2}\s*/\s*\d{4})"], # month/dd/yyyy
        ["%B/%d/%y",r"((january|february|march|april|may|june|july|august|september|october|november|december)\s*/\s*\d{1,2}\s*/\s*\d{2})"], # month/dd/yy
        ["%b/%d/%Y",r"((jan|feb|mar|apr|jun|jul|aug|sep|sept|oct|nov|dec)\s*/\s*\d{1,2}\s*/\s*\d{4})"], # month/dd/yyyy
        ["%b/%d/%y",r"((jan|feb|mar|apr|jun|jul|aug|sep|sept|oct|nov|dec)\s*/\s*\d{1,2}\s*/\s*\d{2})"], # month/dd/yy
        ["%B-%d-%Y",r"((january|february|march|april|may|june|july|august|september|october|november|december)\s*-\s*\d{1,2}\s*-\s*\d{4})"], # month-dd-yyyy
        ["%B-%d-%y",r"((january|february|march|april|may|june|july|august|september|october|november|december)\s*-\s*\d{1,2}\s*-\s*\d{2})"], # month-dd-yy
        ["%b-%d-%Y",r"((jan|feb|mar|apr|jun|jul|aug|sep|sept|oct|nov|dec)\s*-\s*\d{1,2}\s*-\s*\d{4})"], # month-dd-yyyy
        ["%b-%d-%y",r"((jan|feb|mar|apr|jun|jul|aug|sep|sept|oct|nov|dec)\s*-\s*\d{1,2}\s*-\s*\d{2})"], # month-dd-yy
        ["%B.%d.%Y",r"((january|february|march|april|may|june|july|august|september|october|november|december)\s*\.\s*\d{1,2}\s*\.\s*\d{4})"], # month.dd.yyyy
        ["%B.%d.%y",r"((january|february|march|april|may|june|july|august|september|october|november|december)\s*\.\s*\d{1,2}\s*\.\s*\d{2})"], # month.dd.yyyy
        ["%b.%d.%Y",r"((jan|feb|mar|apr|jun|jul|aug|sep|sept|oct|nov|dec)\s*\.\s*\d{1,2}\s*\.\s*\d{4})"], # month.dd.yyyy
        ["%b.%d.%y",r"((jan|feb|mar|apr|jun|jul|aug|sep|sept|oct|nov|dec)\s*\.\s*\d{1,2}\s*\.\s*\d{2})"], # month.dd.yy

        ["%B %d %Y",r"((january|february|march|april|may|june|july|august|september|october|november|december)\s+\d{1,2}\s+\d{4})"], # monthddyyyy
        ["%B %d %y",r"((january|february|march|april|may|june|july|august|september|october|november|december)\s+\d{1,2}\s+\d{2})"], # monthddyyyy
        ["%b %d %Y",r"((jan|feb|mar|apr|jun|jul|aug|sep|sept|oct|nov|dec)\s+\d{1,2}\s+\d{4})"], # monthddyyyy
        ["%b %d %y",r"((jan|feb|mar|apr|jun|jul|aug|sep|sept|oct|nov|dec)\s+\d{1,2}\s+\d{2})"], # monthddyy

        ["%B/%d/%Y",r"((january|february|march|april|may|june|july|august|september|october|november|december)\s*/\s*\d{1,2}(th|st|nd|rd)\s*/\s*\d{4})"], # month/dd(th|st|nd|rd)?/yyyy
        ["%B/%d/%y",r"((january|february|march|april|may|june|july|august|september|october|november|december)\s*/\s*\d{1,2}(th|st|nd|rd)\s*/\s*\d{2})"], # month/dd(th|st|nd|rd)?/yy
        ["%b/%d/%Y",r"((jan|feb|mar|apr|jun|jul|aug|sep|sept|oct|nov|dec)\s*/\s*\d{1,2}(th|st|nd|rd)\s*/\s*\d{4})"], # month/dd(th|st|nd|rd)?/yyyy
        ["%b/%d/%y",r"((jan|feb|mar|apr|jun|jul|aug|sep|sept|oct|nov|dec)\s*/\s*\d{1,2}(th|st|nd|rd)\s*/\s*\d{2})"], # month/dd(th|st|nd|rd)?/yy

        ["%B-%d-%Y",r"((january|february|march|april|may|june|july|august|september|october|november|december)\s*-\s*\d{1,2}(th|st|nd|rd)\s*-\s*\d{4})"], # month-dd(th|st|nd|rd)?-yyyy
        ["%B-%d-%y",r"((january|february|march|april|may|june|july|august|september|october|november|december)\s*-\s*\d{1,2}(th|st|nd|rd)\s*-\s*\d{2})"], # month-dd(th|st|nd|rd)?-yy
        ["%b.%d.%Y",r"((jan|feb|mar|apr|jun|jul|aug|sep|sept|oct|nov|dec)\s*\.\s*\d{1,2}(th|st|nd|rd)\s*\.\s*\d{4})"], # month.dd(th|st|nd|rd)?.yyyy
        ["%b.%d.%y",r"((jan|feb|mar|apr|jun|jul|aug|sep|sept|oct|nov|dec)\s*\.\s*\d{1,2}(th|st|nd|rd)\s*\.\s*\d{2})"], # month.dd(th|st|nd|rd)?.yy

        ["%B %d %Y",r"((january|february|march|april|may|june|july|august|september|october|november|december)\s+\d{1,2}(th|st|nd|rd)\s+\d{4})"], # monthdd(th|st|nd|rd)yyyy
        ["%B %d %y",r"((january|february|march|april|may|june|july|august|september|october|november|december)\s+\d{1,2}(th|st|nd|rd)\s+\d{2})"], # monthdd(th|st|nd|rd)yyyy
        ["%b %d %Y",r"((jan|feb|mar|apr|jun|jul|aug|sep|sept|oct|nov|dec)\s+\d{1,2}(th|st|nd|rd)\s+\d{4})"], # monthdd(th|st|nd|rd)yyyy
        ["%b %d %y",r"((jan|feb|mar|apr|jun|jul|aug|sep|sept|oct|nov|dec)\s+\d{1,2}(th|st|nd|rd)\s+\d{2})"], # monthdd(th|st|nd|rd)yy
        ["%B %d %Y",r"((january|february|march|april|may|june|july|august|september|october|november|december)\s+\d{1,2}(th|st|nd|rd)\s+\d{4})"], # month dd yyyy
        ["%B %d %y",r"((january|february|march|april|may|june|july|august|september|october|november|december)\s+\d{1,2}(th|st|nd|rd)\s+\d{2})"], # month dd yy
        ["%b %d %Y",r"((jan|feb|mar|apr|jun|jul|aug|sep|sept|oct|nov|dec)\s+\d{1,2}(th|st|nd|rd)\s+\d{4})"], # month dd yyyy
        ["%b %d %y",r"((jan|feb|mar|apr|jun|jul|aug|sep|sept|oct|nov|dec)\s+\d{1,2}(th|st|nd|rd)\s+\d{2})"], # month dd yy


        ["%B-%Y",r"((january|february|march|april|may|june|july|august|september|october|november|december)-\d{4})"], # month-yyyy
        ["%B-%y",r"((january|february|march|april|may|june|july|august|september|october|november|december)-\d{2})"], # month-yy
        ["%b-%Y",r"((jan|feb|mar|apr|jun|jul|aug|sep|sept|oct|nov|dec)-\d{4})"], # month-yyyy
        ["%b-%y",r"((jan|feb|mar|apr|jun|jul|aug|sep|sept|oct|nov|dec)-\d{2})"], # month-yy
        ["%B/%Y",r"((january|february|march|april|may|june|july|august|september|october|november|december)/\d{4})"], # month/yyyy
        ["%B/%y",r"((january|february|march|april|may|june|july|august|september|october|november|december)/\d{2})"], # month/yy
        ["%b/%Y",r"((jan|feb|mar|apr|jun|jul|aug|sep|sept|oct|nov|dec)/\d{4})"], # month/yyyy
        ["%b/%y",r"((jan|feb|mar|apr|jun|jul|aug|sep|sept|oct|nov|dec)/\d{2})"], # month/yy
        ["%B.%Y",r"((january|february|march|april|may|june|july|august|september|october|november|december)\.\d{4})"], # month.yyyy
        ["%B.%y",r"((january|february|march|april|may|june|july|august|september|october|november|december)\.\d{2})"], # month.yyyy
        ["%b.%Y",r"((jan|feb|mar|apr|jun|jul|aug|sep|sept|oct|nov|dec)\.\d{4})"], # month.yyyy
        ["%b.%y",r"((jan|feb|mar|apr|jun|jul|aug|sep|sept|oct|nov|dec)\.\d{2})"], # month.yy
        ["%B %Y",r"((january|february|march|april|may|june|july|august|september|october|november|december)\s+\d{4})"], # month yyyy
        ["%B %y",r"((january|february|march|april|may|june|july|august|september|october|november|december)\s+\d{2})"], # month yy
        ["%b %Y",r"((jan|feb|mar|apr|jun|jul|aug|sep|sept|oct|nov|dec)\s*\d{4})"], # month yyyy
        ["%b %y",r"((jan|feb|mar|apr|jun|jul|aug|sep|sept|oct|nov|dec)\s*\d{2})"], # month yy

        ["%Y/%m/%d",r"(\d{4}\s*/\s*\d{1,2}\s*/\s*\d{1,2})"], # yyyy/mm/dd
        ["%Y-%m-%d",r"(\d{4}\s*-\s*\d{1,2}\s*-\s*\d{1,2})"], # yyyy-mm-dd
        ["%Y.%m.%d",r"(\d{4}\s*\.\s*\d{1,2}\s*\.\s*\d{1,2})"], # yyyy.mm.dd
        ["%Y %m %d",r"(\d{4}\s+\d{1,2}\s+\d{1,2})"], # yyyy mm dd
        ["%Y %B %d",r"(\d{4}\s+(january|february|march|april|may|june|july|august|september|october|november|december)\s+\d{1,2})"], # yyyy month dd
        ["%Y %b %d",r"(\d{4}\s+(jan|feb|mar|apr|jun|jul|aug|sep|sept|oct|nov|dec)\s+\d{1,2})"], # yyyy month dd


        ["%Y/%m",r"(\d{4}\s*/\s*\d{1,2})"], # yyyy/mm
        ["%Y-%m",r"(\d{4}\s*-\s*\d{1,2})"], # yyyy-mm
        ["%Y.%m",r"(\d{4}\s*\.\s*\d{1,2})"], # yyyy.mm
        ["%Y %m",r"(\d{4}\s+\d{1,2})"], # yyyy mm

        ["%Y/%B",r"(\d{4}\s*/\s*(january|february|march|april|may|june|july|august|september|october|november|december))"], # yyyy/mm
        ["%Y/%b",r"(\d{4}\s*/\s*(jan|feb|mar|apr|jun|jul|aug|sep|sept|oct|nov|dec))"], # yyyy/mm
        ["%Y-%B",r"(\d{4}\s*-\s*(january|february|march|april|may|june|july|august|september|october|november|december))"], # yyyy-mm
        ["%Y-%B",r"(\d{4}\s*-\s*(jan|feb|mar|apr|jun|jul|aug|sep|sept|oct|nov|dec))"], # yyyy-mm
        ["%Y.%B",r"(\d{4}\s*\.\s*(january|february|march|april|may|june|july|august|september|october|november|december))"], # yyyy.mm
        ["%Y.%b",r"(\d{4}\s*\.\s*(jan|feb|mar|apr|jun|jul|aug|sep|sept|oct|nov|dec))"], # yyyy.mm
        ["%Y %B",r"(\d{4}\s+(january|february|march|april|may|june|july|august|september|october|november|december))"], # yyyy mm
        ["%Y %b",r"(\d{4}\s+(jan|feb|mar|apr|jun|jul|aug|sep|sept|oct|nov|dec))"], # yyyy mm

]