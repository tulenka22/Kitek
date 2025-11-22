<template>
  <block-ab :title="nametitle">
    <div v-safe-html="loadedPage" />
    <div class="hiden">
      <div v-for="us in nameNews" :key="us.id">
        <p v-if="us.id == nameid">{{ (nametitle = us.title) }}</p>
      </div>
    </div>
  </block-ab>
</template>

<script>
import { loadDynamic } from '~/core/helpers/file'
export default {
  async asyncData({ params, error }) {
    const newsJson = JSON.parse(await loadDynamic('dynamic/news/news.json'))
    const newsItem = newsJson.find((item) => item.id == params.id)

    return {
      newsItem,
    }
  },
  data() {
    return {
      nameNews: [],
      nametitle: '',
      nameid: this.$route.params.id,
      loadedPage: 'Загрузка...',
    }
  },
  async created() {
    try {
      this.loadedPage = await loadDynamic(`dynamic/news/${this.id}.html`)
      this.nameNews = JSON.parse(await loadDynamic('dynamic/news/news.json'))
    } catch {
      this.loadedPage = 'Ошибка при загрузке динамической страницы.'
    }
  },
  computed: {
    id() {
      return this.$route.params.id
    },
  },
  head() {
    return {
      title: this.newsItem.title,
      meta: [
        {
          hid: 'keywords',
          name: 'keywords',
          content: this.newsItem.keywords,
        },
        {
          hid: 'description',
          name: 'description',
          content: this.newsItem.description,
        },
        { hid: 'title', name: 'title', content: this.newsItem.title },
        // Other meta tags
      ],
    }
  },
}
</script>

<style scoped lang="scss">
.hiden {
  display: none;
}
</style>
