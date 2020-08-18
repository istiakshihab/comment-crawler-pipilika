def trim_title(title):
    ret_str = ""

    for ch in title:
        if ch == ':' or ch == 'ঃ' or ch == ',':
            return ret_str
        ret_str += ch
    return ret_str

#UniqueID,Text/Data,Type, Domain,RootURL,DataSource,Datapublishdate(Optional),Parse/Scrapetime.

def return_items(uid, comment, category, url, rootdomain, publishdate, parsetime, source="newspaper",datadomain=""):
    
    item = {
        'UniqueID': uid,
        'Text':comment,
        'Type': category,
        'Domain': datadomain,
        'url': url,
        'RootDomain': rootdomain,
        'source': source,
        'DataPublishDate':publishdate,
        'ParseTime': parsetime,
    }
    return item
