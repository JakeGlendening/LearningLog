from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Topic,Entry
class LearningLogTests(TestCase):
 def setUp(self):
  self.a=User.objects.create_user(username='alice',password='SafePass12345')
  self.b=User.objects.create_user(username='bob',password='SafePass12345')
  self.topic=Topic.objects.create(text='Chess',owner=self.a)
  self.entry=Entry.objects.create(topic=self.topic,text='Learned openings')
 def test_home_public(self):self.assertEqual(self.client.get('/').status_code,200)
 def test_topics_requires_login(self):self.assertEqual(self.client.get(reverse('MainApp:topics')).status_code,302)
 def test_own_topic_visible(self):
  self.client.force_login(self.a)
  self.assertContains(self.client.get(reverse('MainApp:topic',args=[self.topic.id])),'Learned openings')
 def test_other_topic_inaccessible(self):
  self.client.force_login(self.b)
  self.assertEqual(self.client.get(reverse('MainApp:topic',args=[self.topic.id])).status_code,404)
 def test_other_entry_edit_inaccessible(self):
  self.client.force_login(self.b)
  self.assertEqual(self.client.get(reverse('MainApp:edit_entry',args=[self.entry.id])).status_code,404)
 def test_other_topic_new_entry_inaccessible(self):
  self.client.force_login(self.b)
  self.assertEqual(self.client.get(reverse('MainApp:new_entry',args=[self.topic.id])).status_code,404)
 def test_new_topic_ownership(self):
  self.client.force_login(self.b)
  self.client.post(reverse('MainApp:new_topic'),{'text':'Python'})
  self.assertTrue(Topic.objects.filter(text='Python',owner=self.b).exists())
 def test_edit_own_entry(self):
  self.client.force_login(self.a)
  self.client.post(reverse('MainApp:edit_entry',args=[self.entry.id]),{'text':'Updated lesson'})
  self.entry.refresh_from_db()
  self.assertEqual(self.entry.text,'Updated lesson')
