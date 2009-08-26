# Copyright 2009 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.conf.urls.defaults import *

urlpatterns = patterns('',
  # General URL handlers in shared/util.py
  (r'^$', 'base.util.Home'),
  (r'^faq', 'base.util.Faq'),
  (r'^alltests', 'base.util.AllTests'),
  (r'^beacon.*', 'base.util.Beacon'),
  (r'^get_csrf',  'base.util.GetCsrf'),

  # Admin functionality
  (r'^update_datastore', 'base.util.UpdateDatastore'),
  (r'^seed_datastore$', 'base.util.SeedDatastore'),
  (r'^clear_datastore$', 'base.util.ClearDatastore'),
  (r'^clear_memcache',  'base.util.ClearMemcache'),
  (r'^admin$', 'base.admin.Admin'),
  (r'^admin/confirm-ua', 'base.admin.ConfirmUa'),
  (r'^admin/stats', 'base.admin.Stats'),
  (r'^admin/rankers/all$', 'base.admin_rankers.AllRankers'),
  (r'^admin/update_result_parents?', 'base.admin_rankers.UpdateResultParents'),
  (r'^admin/update_dirty$', 'base.manage_dirty.UpdateDirty'),
  (r'^admin/make_dirty$', 'base.manage_dirty.MakeDirty'),
  (r'^admin/user_agents.csv$', 'base.util.UserAgents'),

  # Cron admin scripts
  (r'^cron/user_agent_group$', 'base.cron.UserAgentGroup'),
  (r'^cron/update_recent_tests$', 'base.cron.UpdateRecentTests'),

  (r'^_ah/queue/update-dirty', 'base.manage_dirty.UpdateDirty'),
  (r'^_ah/queue/user-agent-group$', 'base.cron.UserAgentGroup'),
  (r'^_ah/queue/recent-tests$', 'base.cron.UpdateRecentTests'),

  # GAEBar
  (r'^gaebar/', include('third_party.gaebar.urls')),

  # UNIT TEST URLs
  # TODO(elsigh): try to do a custom urls.py for unit tests?
  (r'^fake_check_csrf',  'base.util.FakeCheckCsrf'),


  #############################################################################
  ## CATEGORY URLS BELOW
  #############################################################################

  # Reflow Timer URLs
  (r'^reflows?/?$', 'categories.reflow.handlers.About'),
  (r'^reflow/about$', 'categories.reflow.handlers.About'),
  (r'^reflow/test$', 'categories.reflow.handlers.Test'),
  (r'^reflow/test_selectors$', 'categories.reflow.handlers.TestSelectors'),
  (r'^reflow/test_gen_css$', 'categories.reflow.handlers.TestGenCss'),
  (r'^reflow/test/nested_tables$', 'categories.reflow.handlers.NestedTables'),
  (r'^reflow/test/nested_divs$', 'categories.reflow.handlers.NestedDivs'),
  (r'^reflow/test/nested_anchors$', 'categories.reflow.handlers.NestedAnchors'),
  (r'^reflow/stats_chart$', 'categories.reflow.handlers.StatsChart'),
  (r'^reflow/stats_table$', 'categories.reflow.handlers.StatsTable'),
  (r'^reflow/locations', 'categories.reflow.handlers.Locations'),

  # Network Performance main URLs
  (r'^network/?$', 'categories.network.handlers.About'),
  (r'^network/about$', 'categories.network.handlers.About'),
  (r'^network/test$', 'categories.network.handlers.Test'),
  (r'^network/testdriver', 'categories.network.handlers.TestDriver'),
  (r'^network/stats_table$', 'categories.network.handlers.StatsTable'),

  # Network Performance test URLs
  (r'^network/tests/cache-expires2', 'categories.network.handlers.CacheExpires2'),
  (r'^network/tests/cache-expires', 'categories.network.handlers.CacheExpires'),
  (r'^network/tests/cache-redirects2', 'categories.network.handlers.CacheRedirects2'),
  (r'^network/tests/cache-redirects', 'categories.network.handlers.CacheRedirects'),
  (r'^network/tests/cache-resource-redirects2', 'categories.network.handlers.CacheResourceRedirects2'),
  (r'^network/tests/cache-resource-redirects', 'categories.network.handlers.CacheResourceRedirects'),
  (r'^network/tests/connections-per-hostname', 'categories.network.handlers.ConnectionsPerHostname'),
  (r'^network/tests/data-urls', 'categories.network.handlers.DataUrls'),
  (r'^network/tests/gzip', 'categories.network.handlers.Gzip'),
  (r'^network/tests/inline-script-after-stylesheet', 'categories.network.handlers.InlineScriptAfterStylesheet'),
  (r'^network/tests/latency', 'categories.network.handlers.Latency'),
  (r'^network/tests/link-prefetch2', 'categories.network.handlers.LinkPrefetch2'),
  (r'^network/tests/link-prefetch', 'categories.network.handlers.LinkPrefetch'),
  (r'^network/tests/max-connections', 'categories.network.handlers.MaxConnections'),
  (r'^network/tests/scripts-block', 'categories.network.handlers.ScriptsBlock'),
  (r'^network/tests/stylesheets-block', 'categories.network.handlers.StylesheetsBlock'),
  # Network Performance admin URLs
  (r'^network/admin', 'categories.network.handlers.Admin'),
  (r'^network/confirm-ua', 'categories.network.handlers.ConfirmUa'),
  (r'^network/stats', 'categories.network.handlers.Stats'),
  (r'^network/loader', 'categories.network.handlers_loader.ResultLoader'),

  # Acid3 Test URLs
  (r'acid3/?$', 'categories.acid3.handlers.About'),
  (r'acid3/about$', 'categories.acid3.handlers.About'),
  (r'acid3/test$', 'categories.acid3.handlers.Test'),
  (r'acid3/support-a.png$', 'categories.acid3.handlers.SupportAPng'),

  # Selectors API Test URLs
  (r'selectors/?$', 'categories.selectors.handlers.About'),
  (r'selectors/about$', 'categories.selectors.handlers.About'),
  (r'selectors/test$', 'categories.selectors.handlers.Test'),

  # v8 Benchmark Suite URLs
  (r'v8/?$', 'categories.v8.handlers.About'),
  (r'v8/about$', 'categories.v8.handlers.About'),
  (r'v8/test$', 'categories.v8.handlers.Test'),

  # SunSpider Benchmark Suite URLs
  (r'sunspider/?$', 'categories.sunspider.handlers.About'),
  (r'sunspider/about$', 'categories.sunspider.handlers.About'),
  (r'sunspider/test$', 'categories.sunspider.handlers.Test'),

  # Rich text urls
  (r'^richtext/tests', 'categories.richtext.handlers.RunTests'),
  (r'^richtext/apply-tests', 'categories.richtext.handlers.Apply'),
  (r'^richtext/unapply-tests', 'categories.richtext.handlers.Unapply'),
  (r'^richtext/query-tests', 'categories.richtext.handlers.QueryCommand'),
  (r'^richtext/change-tests', 'categories.richtext.handlers.Change'),
  (r'^richtext/editable', 'categories.richtext.handlers.EditableIframe'),

)