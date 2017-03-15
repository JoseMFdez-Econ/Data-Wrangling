# To experiment with this code freely you will have to run this code locally.
# Take a look at the main() function for an example of how to use the code.
# We have provided example json output in the other code editor tabs for you to
# look at, but you will not be able to run any queries through our UI.
import json
import requests
import os
import re # Regular Expressions library

os.chdir("/Users/josemanuelfernandez/Documents/Udacity/Data_Analyst/P3/Data-Wrangling/Lesson-1/coursera")



BASE_URL = "http://musicbrainz.org/ws/2/"
ARTIST_URL = BASE_URL + "artist/" # That is: http://musicbrainz.org/ws/2/artist/

# query parameters are given to the requests.get function as a dictionary; this
# variable contains some starter parameters.
query_type = {  "simple": {},
                "atr": {"inc": "aliases+tags+ratings"},
                "aliases": {"inc": "aliases"},
                "releases": {"inc": "releases"}}


def query_site(url, params, uid="", fmt="json"):
    # This is the main function for making queries to the musicbrainz API.
    # A json document should be returned by the query.
    params["fmt"] = fmt
    r = requests.get(url + uid, params=params)
    # params >> {'fmt': 'json', 'inc': 'releases'}
    print ("requesting url", r.url)
    #>> requesting http://musicbrainz.org/ws/2/artist/a23cf927-b533-47e9-a453-384765afb3b1?fmt=json&inc=releases
    #print ("PARAMETERS in query_site() !!!! :", params)

    #print ("STATUS_CODE: ", r.status_code) # >> 200
    #print ("REQUESTS.CODES.OK: ", requests.codes.ok) # >> 200
    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        r.raise_for_status()


def query_by_name(url, params, name):
    # This adds an artist name to the query parameters before making
    # an API call to the function above.

    #print ("PARAMETERS in query_by_name() !!!! :", params) # >> {} -> Returns empty list
    params["query"] = "artist:" + name
    #print ("PARAMETERS in query_by_name() !!!! :", params) # >> {'query': 'artist:Los Van Van'}
    return query_site(url, params)


def pretty_print(data, indent=4):
    # After we get our output, we can format it to be more readable
    # by using this function.
    if type(data) == dict:
        print (json.dumps(data, indent=indent, sort_keys=True))
    else:
        print (data)


def main():
    '''
    Modify the function calls and indexing below to answer the questions on
    the next quiz. HINT: Note how the output we get from the site is a
    multi-level JSON document, so try making print statements to step through
    the structure one level at a time or copy the output to a separate output
    file.
    '''
    # ARTIST_URL -> http://musicbrainz.org/ws/2/artist/
    # query_type["simple"] (line 19 above)-> "simple": {}
    # name of Artist (name) -> "Los Van Van"
    results = query_by_name(ARTIST_URL, query_type["simple"], "One Direction")
    #pretty_print(results)

    #print ("CLASS for 'results': ", type(results))
    #print ("CLASS for results[artists]: ", type(results["artists"]))
    #print ("Length of LIST -> results[artists]: ",len(results["artists"]))

    #print ("CLASS for results[artists][index]: ", type(results["artists"][0]))
    #print("LIST of keys in DICT results[artists][0]: ",results["artists"][0].keys())
    #print("LIST of keys in DICT results[artists][1]: ",results["artists"][1].keys())


    #results = query_by_name(ARTIST_URL, query_type["simple"], "One Direction")
    for item in range(len(results["artists"])):
        if results["artists"][item]["score"] == "100":
            print (results["artists"][item]["life-span"]["begin"]) # >> 2010-07

'''
    ## Disambiguation for "Nirvana"
    print("LIST/DICT ",results["artists"][4]["area"]["name"])
    pretty_print ((results["artists"][4]["disambiguation"]))
'''


'''
    # Gets 'unique id' for the artist of interest
    artist_id = results["artists"][1]["id"]
    print ("\nARTIST:")
    pretty_print(results["artists"][1])

    artist_data = query_site(ARTIST_URL, query_type["releases"], artist_id)
    releases = artist_data["releases"]
    print ("\nONE RELEASE:")
    pretty_print(releases[0], indent=2)
    release_titles = [r["title"] for r in releases]

    print ("\nALL TITLES:")
    for t in release_titles:
        print (t)
'''

'''
    ## Total Bands called "First Aid Kit" - #1
    #results = query_by_name(ARTIST_URL, query_type["simple"], "First Aid Kit")
    list_id = list()
    for artist in results["artists"]:
        if artist["name"] == "First Aid Kit":
            list_id.append(artist["id"])
        total = len(list_id)
    print (total)
'''

'''
    ## Total Bands called "First Aid Kit" - #2
    count = 0
    for item in range(len(results["artists"])):
        if results["artists"][item]["name"] == "First Aid Kit":
            count +=1
    print(count) # >> 2
'''

'''
    ## Begin-Area for the Band Queen
    #results = query_by_name(ARTIST_URL, query_type["simple"], "Queen")
    begin_area = list()
    for item in range(len(results["artists"])):
         if results["artists"][item]["name"] == "Queen":
             if (results["artists"][item]["disambiguation"]) == "UK rock group":
                 begin_area.append(results["artists"][item]["begin-area"]["name"])
    print ("Begin-Area for the Band Queen is: ",begin_area[0]) # >> London
'''

'''
    ## Spanish Alias for "The Beatles"
    #results = query_by_name(ARTIST_URL, query_type["simple"], "The Beatles")
    for item in range(len(results["artists"])):
         if results["artists"][item]["name"] == "The Beatles":
             alias_list = results["artists"][item]["aliases"]
             for alias in alias_list:
                 if alias["locale"] == 'es':
                     print (alias["name"]) # >> Los Beatles
'''


if __name__ == '__main__':
    main()
