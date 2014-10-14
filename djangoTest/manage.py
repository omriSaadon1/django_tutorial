#!/usr/bin/env python
import os
import sys
from polls.models import Poll, Choice
from django.utils import timezone
if __name__ == "__main__":

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoTest.settings")

    from django.core.management import execute_from_command_line
    # p = Poll.objects.get(pk=1)
    # #print p.was_published_recently()
    # #p.choice_set.create(choice_text='boy', votes=0)
    # #p.choice_set.create(choice_text='cell', votes=0)
    # #c = p.choice_set.create(choice_text='compability', votes=0)
    # #print c.poll
    #print Poll.objects.get(id=3)
    # print p.choice_set.all()
    #Poll.delete(Poll.objects.get(id=2))
    # #print p.choice_set.count()
    # # c = p.choice_set.filter(id=1)
    # # c.delete()
    # # for i in range(1,9):
    # #     c = p..filter(id=i)
    # #     c.delete()
    # print Poll.objects.all()
    # p = Poll(question="What's new?", pub_date=timezone.now())
    # p.save()
    # p.choice_set.create(choice_text='nice', votes=0)
    # p.choice_set.create(choice_text='bad', votes=0)
    # import sys
    # sys.path = sys.path[1:]
    # import django
    # print(django.__path__)
    # from django.test.utils import setup_test_environment
    # setup_test_environment()
    # from django.test.client import Client
    # client = Client()
    # # get a response from '/'
    # response = client.get('/')
    # # we should expect a 404 from that address
    # print response.status_code
    # #404
    # # on the other hand we should expect to find something at '/polls/'
    # # we'll use 'reverse()' rather than a hardcoded URL
    # from django.core.urlresolvers import reverse
    # response = client.get(reverse('polls:index'))
    # print response.status_code
    # #200
    # print response.content
    # '\n\n\n    <p>No polls are available.</p>\n\n'
    # # note - you might get unexpected results if your ``TIME_ZONE``
    # # in ``settings.py`` is not correct. If you need to change it,
    # # you will also need to restart your shell session
    # from polls.models import Poll
    # from django.utils import timezone
    # # create a Poll and save it
    # #p = Poll(question="Who is your favorite Beatle?", pub_date=timezone.now())
    # #p.save()
    # # check the response once again
    # response = client.get('/polls/')
    # print response.content
    # #n\n    <ul>\n    \n        <li><a href="/polls/1/">Who is your favorite Beatle?</a></li>\n    \n    </ul>\n\n'
    # # If the following doesn't work, you probably omitted the call to
    # # setup_test_environment() described above
    # #print response.context['latest_poll_list']
    # #[<Poll: Who is your favorite Beatle?>]
    execute_from_command_line(sys.argv)

