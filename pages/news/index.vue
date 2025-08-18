<template>
  <block-ab title="Новости">
    <div>
      <div class="news">
        <EntitiesNewCard v-for="(n, nIdx) in visibleNews" :key="nIdx" :instance="n" />
        <button class="btn el__btn btn-red" @click="loadMore">Загрузить еще</button>
      </div>
    </div>
  </block-ab>
</template>

<script>
import { loadDynamic } from '~/core/helpers/file'

export default {
  async created() {
    try {
      this.news = JSON.parse(await loadDynamic('dynamic/news/news.json'))
    } catch {
      console.log('Проверьте валидность JSON новостей и событий!')
    }
  },
  data() {
    return {
      news: [],
      displayedNews: 10, // Первоначально отображаем только 10 новостей
    }
  },
  computed: {
    // Сортировка всех новостей по дате
    sortedNews() {
      return this.news.sort((a, b) => new Date(b.date) - new Date(a.date))
    },
    // Отображаемые новости
    visibleNews() {
      return this.sortedNews.slice(0, this.displayedNews)
    },
  },
  methods: {
    loadMore() {
      this.displayedNews += 10 // При нажатии "Загрузить еще" добавляем следующие 10 новостей к отображаемым
    },
  },
}
</script>

<style scoped lang="scss">
.news {
  max-width: 1400px;
  transition: $t grid-template-columns;
  display: block;
  grid-template-columns: 0.7fr 0.3fr;
  gap: 0 32px;
  @media screen and (max-width: 1200px) {
    display: block;
    .news__self {
      margin-bottom: 32px;
    }
  }
}
.btn {
  margin-top: 15px;
  transition: $t background-color;
  border-radius: 8px;
  @extend %tg-h3;
  padding: 12px 48px;
  &-red {
    background-color: $primary-color;
    color: $bg-control;
    &:hover {
      background-color: saturate($primary-color, $amount: 10);
    }
  }
}
</style>
