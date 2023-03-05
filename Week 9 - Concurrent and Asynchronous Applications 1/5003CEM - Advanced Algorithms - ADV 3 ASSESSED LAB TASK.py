import concurrent.futures
import newspaper
from newspaper import Article
from threading import Lock



data_lock = Lock()                                              #Initialsies "data_lock" with a new instance of "Lock" object from Python "threading" module

URLs = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://www.derspiegel.de/',
        'http://www.bbc.co.uk/',
        'https://theguardian.com',]                             #List of URL's to be accessed to get headlines



'''Define function called "non_concurrent_get_headlines":
   Implements iterativley printing 5 headlines from accessing each URL using a singlethreaded approach w/ No parameters:
'''
def non_concurrent_get_headlines():
    for url in URLs:                                            #For each "url" in "URLs" (-1 as index start at 0)
        result = newspaper.build(url, memoize_articles=False)   #Initalise "result" with a new instance of the "newspaper" object using "build" method and "url" as argument
                                                                #"memoize_articles" parameter prevents caching of articles
        
        print('\n''The headlines from %s are' % url, '\n')      #Print statement detailing the current URL content being displayed, wildcard to replace '%s' with "url"
        for i in range(1,6):                                    #Iterate over the same code block 5 times, 'i' initialised with '1' and incremented after each loop
            art = result.articles[i]                            #Initalise "art" with the 'i'-th element of result containing an article from "url"
            art.download()                                      #Download article content as HTML
            art.parse()                                         #Parse (Extract) article content from downloaded HTML
            print(art.title)                                    #Print the title of the article

'''Define function called "concurrent_get_headlines":
   Implements iterativley printing 5 headlines from accessing each URL using a multithreaded approach w/ No parameters:
'''
def concurrent_get_headlines():


    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
                                                                #"executor" is a pool consisting of a maximum of 5 threads, "executor" executes tasks in parallel
        future_to_url = {executor.submit(newspaper.build, url, memoize_articles=False): url for url in URLs}
                                                                #Initalise "future_to_url" as dictionary with new instances of the "newspaper" object using "build" method 
                                                                #for each "url" from "URLs" as arguments

        for future in concurrent.futures.as_completed(future_to_url):
                                                                #For each "future" in "future_to_url" execute loop code block for each "future" in parallel 
                                                                #as the "newspaper" objects are built using each "url" in "URLs" using ".as_completed()"
                                                                #(Opposed to waiting for each "future" in "future_to_url" to have "newspaper" object built)

            url = future_to_url[future]                         #Set "url" to the "url" of current completed "future" from "future_to_url"
            result = future.result()                            #Set "result" to each completed "future" as it is available

            with data_lock:                                     #Prevent access to "print()" by multiple threads at the same time, ensures articles are printed with headline they're associated with
                print('\n''The headlines from %s are' % url, '\n')
                                                                #Print statement detailing the current URL content being displayed, wildcard to replace '%s' with "url"

                for i in range(1, 6):                           #Iterate over the same code block 5 times, 'i' initialised with '1' and incremented after each loop
                    art = result.articles[i]                    #Initalise "art" with the 'i'-th element of result containing an article from "url"
                    art.download()                              #Download article content as HTML
                    art.parse()                                 #Parse (Extract) article content from downloaded HTML
                    print(art.title)                            #Print the title of the article



if __name__ == '__main__':
    import timeit                                               #Import Python "timeit" module
    


    elapsed_time = timeit.timeit("non_concurrent_get_headlines()", setup="from __main__ import non_concurrent_get_headlines", number=1)
                                                                #Set "elapsed_time" to return value of "timeit()" function, representing time taken to execute "non_concurrent_get_headlines()" function a single time
    print("\n-------------------------------------------\n" + 
          "Time elapased for Non-concurrent execution:\n" + 
          str(elapsed_time) +
          "\n-------------------------------------------\n")    #Print statement detailing execution time of "non_concurrent_get_headlines()" function (Singlethreaded)

    elapsed_time = timeit.timeit("concurrent_get_headlines()", setup="from __main__ import concurrent_get_headlines", number=1)
                                                                #Set "elapsed_time" to return value of "timeit()" function, representing time taken to execute "concurrent_get_headlines()" function a single time
    print("\n---------------------------------------\n" + 
          "Time elapased for Concurrent execution:\n" 
          + str(elapsed_time) +
          "\n---------------------------------------\n")        #Print statement detailing execution time of "concurrent_get_headlines()" function (Multithreaded)