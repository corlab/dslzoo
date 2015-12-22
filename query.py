#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import yaml
import pickle

from scholar import *

# Read input
with open('./src/icinput','r') as inf:
  icinput = yaml.load(inf.read())
  #print icinput

def generateQueries(ic):
  queryParams = []

  conferenceCandidates = icinput[ic]['conferences']
  keywordCandidates = icinput[ic]['keywords']
    
  for conf in conferenceCandidates:
    if conf.strip() != "" and conf.strip()[0] != "#":
      for kword in keywordCandidates:
        if kword.strip() != "" and kword.strip()[0] != "#":
          filename = ic+'_'+conf.strip().lower().replace(' ', '-') + '_' \
            + kword.strip().lower().replace(' ', '-')
          if not os.path.exists('results/'+filename+'.txt'):
            queryParam = [conf.strip(), icinput[ic]['conferences'][conf.strip()]['query'], kword.strip()]
            queryParams.append(queryParam)

  print "Found "+str(len(conferenceCandidates))+" "+ic+" conferences and " \
    +str(len(keywordCandidates))+" "+ic+" keywords, resulting in " \
    +str(len(conferenceCandidates) * len(keywordCandidates)) \
    +" "+ic+" queries to be performed. Skipping " \
    +str(len(conferenceCandidates) * len(keywordCandidates) - len(queryParams)) \
    +" queries because commented out or already performed, so now performing " \
    +str(len(queryParams)) +" remaining "+ic+" queries."

  return queryParams

def main():
  
  # Configure scholar.py
  ScholarConf.LOG_LEVEL = ScholarUtils.LOG_LEVELS['warn']
  ScholarConf.COOKIE_JAR_FILE = './cookie'
  ScholarConf.USER_AGENT = 'Mozilla/5.0 ;Windows NT 6.1; WOW64; Trident/7.0; rv:11.0;h'
  settings = ScholarSettings()
  settings.set_citation_format(ScholarSettings.CITFORM_BIBTEX)
  
  # Get queries to perform
  IC1Queries = generateQueries("IC1")
  IC2Queries = generateQueries("IC2")
  num_queries = (len(IC1Queries) + len(IC2Queries))  
  print '\nNow permorfing '+str(num_queries)+' queries.\n'
    
  icQueries = {'IC1': IC1Queries, 'IC2': IC2Queries}
  
  for ic in icQueries:
  
    # Perform robotics queries
    for pair in icQueries[ic]:
      print pair

      # prepare log to dump into result file
      log = {}
      log['ic'] = ic
      log['conference'] = pair[0]
      log['phrase'] = pair[1]
      log['keyword'] = pair[2]
    
      filename = ic+'_'+pair[0].lower().replace(' ', '-') + '_' \
              + pair[2].lower().replace(' ', '-')
      cfile = open('results/'+filename+'.txt', 'wa')
      results = []
      
      # Get results, until result of page is < ScholarConf.MAX_PAGE_RESULTS
      paging = 0
      do_paging = True
      while do_paging:
        # Set up scholar.py querier
        querier = ScholarQuerier()
        querier.apply_settings(settings)
        query = SearchScholarQuery()
        query.set_pub(pair[1])
        query.set_phrase(pair[2])
        query.set_num_page_results(ScholarConf.MAX_PAGE_RESULTS)
        query.set_start(paging * ScholarConf.MAX_PAGE_RESULTS)

        # perform query
        querier.send_query(query)
        if paging == 0:
          log['query'] = query.get_url()
        
        # Check if more than ScholarConf.MAX_PAGE_RESULTS, then have to page
        if len(querier.articles) >= ScholarConf.MAX_PAGE_RESULTS:
          do_paging = True
        else:
          do_paging = False

        # Loop through results
        print ' '+str(len(querier.articles))+' results on page '+str(paging+1)+' for \"'+pair[2]+'\" on '+pair[0]
        for article in querier.articles:
          if article['title'] and article['year']:
            results.append(article)
            
        paging = paging + 1
        # pause for an appropriate time to not flood google scholar with queries
          
      # dump query results
      log['articles'] = results
      pickle.dump(log, cfile)
  
  print "All done!"

  return 0

if __name__ == "__main__":
  sys.exit(main())

