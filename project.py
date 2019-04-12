#!/usr/bin/env python2
import psycopg2


# connect Database
def data_db(sql_request):
    conn = psycopg2.connect(database="news")
    c = conn.cursor()
    c.execute(sql_request)
    results = c.fetchall()
    conn.close()
    return results

# Q 1: What are the three most popular articles of all time?
answer_1 = '''select articles.title, count(*) as num
            from articles, log
            where log.status='200 OK'
            and articles.slug = substr(log.path, 10)
            group by articles.title
            order by num desc limit 3;'''


# Q 2: Who are the most popular article authors of all time?
answer_2 = '''select authors.name, count(*) as num
            from articles, log, authors
            where log.status='200 OK'
            and authors.id = articles.author
            and articles.slug = substr(log.path, 10)
            group by authors.name
            order by num desc;'''

# Q 3: On which day did more than 1% of requests lead to errors?
answer_3 = '''select down.sys, round((100.0*down.error/down.total),2) as fault
              from
              (select date_trunc('day', time) as sys,
              count(id) as total,
              sum(case when status!='200 OK' then 1 else 0 end) as error
              from log
              group by sys) as down
              where round((100.0*down.error/down.total),2) >1;'''

# Writing a report
# Print the most popular articles
print 'The three most popular articles of all time :'


def most(sql_request):
    articles = data_db(sql_request)
    for article in articles:
        print str(article[0]) + ' : ' + str(article[1])
most(answer_1)

# Print the most popular authors
print 'The most popular article authors of all time :'


def popular(sql_request):
    authors = data_db(sql_request)
    for author in authors:
        print str(author[0]) + ' : ' + str(author[1])
popular(answer_2)

# print errors days
print 'The percent of days errors :'


def days(sql_request):
    errors = data_db(sql_request)
    for error in errors:
        print str(error[0]) + ' : ' + str(error[1]) + '%'
days(answer_3)
