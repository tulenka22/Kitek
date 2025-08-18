<template>
  <block-ab title="Поиск">
    <div class="ya-site-form ya-site-form_inited_no" data-bem="{dataBemSerch}">
      <form
        action="https://yandex.ru/search/site/"
        method="get"
        target="_blank"
        accept-charset="utf-8">
        <input type="hidden" name="searchid" value="2819116" /><input
          type="hidden"
          name="l10n"
          value="ru" /><input type="hidden" name="reqenc" value="" /><input
          class="search"
          type="search"
          name="text"
          value="" /><input class="submit" type="submit" value="Найти" />
      </form>
    </div>
    <div id="ya-site-results" data-bem="{dataBemResult}"></div>
  </block-ab>
</template>

<script type="text/javascript">
var dataBemResult =
  '"{&quot;tld&quot;: &quot;ru&quot;,&quot;language&quot;: &quot;ru&quot;,&quot;encoding&quot;: &quot;&quot;,&quot;htmlcss&quot;: &quot;1.x&quot;,&quot;updatehash&quot;: true}"'
var dataBemSerch =
  '"{&quot;action&quot;:&quot;https://omsktec.ru/search&quot;,&quot;arrow&quot;:false,&quot;bg&quot;:&quot;transparent&quot;,&quot;fontsize&quot;:15,&quot;fg&quot;:&quot;#000000&quot;,&quot;language&quot;:&quot;ru&quot;,&quot;logo&quot;:&quot;rb&quot;,&quot;publicname&quot;:&quot;Поиск&quot;,&quot;suggest&quot;:true,&quot;target&quot;:&quot;_blank&quot;,&quot;tld&quot;:&quot;ru&quot;,&quot;type&quot;:3,&quot;usebigdictionary&quot;:true,&quot;searchid&quot;:2819116,&quot;input_fg&quot;:&quot;#202020&quot;,&quot;input_bg&quot;:&quot;#ffffff&quot;,&quot;input_fontStyle&quot;:&quot;normal&quot;,&quot;input_fontWeight&quot;:&quot;normal&quot;,&quot;input_placeholder&quot;:&quot;&quot;,&quot;input_placeholderColor&quot;:&quot;#000000&quot;,&quot;input_borderColor&quot;:&quot;#acacac&quot;}"'
;(function (w, d, c) {
  var s = d.createElement('script'),
    h = d.getElementsByTagName('script')[0],
    e = d.documentElement
  if ((' ' + e.className + ' ').indexOf(' ya-page_js_yes ') === -1) {
    e.className += ' ya-page_js_yes'
  }
  s.type = 'text/javascript'
  s.async = true
  s.charset = 'utf-8'
  s.src =
    (d.location.protocol === 'https:' ? 'https:' : 'http:') + '//site.yandex.net/v2.0/js/all.js'
  h.parentNode.insertBefore(s, h)
  ;(w[c] || (w[c] = [])).push(function () {
    Ya.Site.Form.init()
  })
})(window, document, 'yandex_site_callbacks')
;(function (w, d, c) {
  var s = d.createElement('script'),
    h = d.getElementsByTagName('script')[0]
  s.type = 'text/javascript'
  s.async = true
  s.charset = 'utf-8'
  s.src =
    (d.location.protocol === 'https:' ? 'https:' : 'http:') + '//site.yandex.net/v2.0/js/all.js'
  h.parentNode.insertBefore(s, h)
  ;(w[c] || (w[c] = [])).push(function () {
    Ya.Site.Results.init()
  })
})(window, document, 'yandex_site_callbacks')
</script>

<style scoped type="text/css">
/* .ya-page_js_yes .ya-site-form_inited_no {
  display: none;
} */
.search {
  border: 1px solid #202020;
  margin: 5px;
  width: 70vw;
}
.submit {
  border: 1px solid #202020;
  margin: 5px;
  padding: 3px;
  font-size: 15px;
  cursor: pointer;
}
.submit ::hover {
  border: 1px solid #ee0000;
}
</style>
