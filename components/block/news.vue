<template>
  <div class="news">
    <AppBlock
      :block-style="{
        maxHeight: '700px',
        minHeight: '700px',
        overflowY: 'auto',
      }"
      :content-style="{
        padding: '24px',
      }"
      class="news__self"
      title="Новости">
      <transition-group name="news-list" tag="div" class="news__list">
        <EntitiesNewCard
          v-for="(n, nIdx) of news"
          :key="n.id || nIdx"
          :instance="n"
          class="news__card" />
      </transition-group>

      <a
        href="https://vk.com/omsktec"
        target="_blank"
        class="news__vk"
        @mouseenter="vkHover = true"
        @mouseleave="vkHover = false"
        :class="{ 'vk-animate': vkHover }"
        aria-label="VK">
        <IconWrapper width="32" height="32">
          <IconVK />
        </IconWrapper>
      </a>

      <a href="/news" class="news__more" aria-label="Все новости"> Все новости </a>
    </AppBlock>

    <AppBlock
      :block-style="{
        maxHeight: '700px',
        minHeight: '700px',
        overflowY: 'auto',
      }"
      :content-style="{
        padding: '24px',
      }"
      class="news__events"
      title="События">
      <transition-group name="news-list" tag="div" class="news__list">
        <EntitiesEventCard
          v-for="(event, eventIdx) of events"
          :key="event.id || eventIdx"
          :instance="event"
          class="news__card" />
      </transition-group>
    </AppBlock>
  </div>
</template>

<script>
import { loadDynamic } from '~/core/helpers/file'
export default {
  name: 'BlockNews',
  data() {
    return {
      events: [],
      news: [],
      vkHover: false,
    }
  },
  async created() {
    try {
      this.events = JSON.parse(await loadDynamic('dynamic/news/events.json'))
      this.news = JSON.parse(await loadDynamic('dynamic/news/news-all.json'))
    } catch {
      console.log('Проверьте валидность JSON новостей и событий!')
    }
  },
}
</script>

<style scoped lang="scss">
.news {
  display: grid;
  grid-template-columns: 0.7fr 0.3fr;
  gap: 0 32px;
  transition: grid-template-columns 0.3s ease;

  @media screen and (max-width: 1200px) {
    display: block;
    .news__self {
      margin-bottom: 32px;
    }
  }

  &__self,
  &__events {
    position: relative;
  }

  /* Анимация появления/исчезновения новостей */
  .news-list-enter-active,
  .news-list-leave-active {
    transition: all 0.4s ease;
  }
  .news-list-enter-from {
    opacity: 0;
    transform: translateY(20px);
  }
  .news-list-leave-to {
    opacity: 0;
    transform: translateY(-20px);
  }

  &__list {
    display: flex;
    flex-direction: column;
    gap: 16px;
  }

  &__card {
    border-radius: 12px;
    background-color: #fff;
    box-shadow: 0 3px 10px rgba(0, 0, 0, 0.07);
    padding: 16px;
    transition: box-shadow 0.3s ease, transform 0.3s ease;
    cursor: pointer;

    &:hover {
      box-shadow: 0 8px 24px rgba(0, 123, 255, 0.15);
      transform: translateY(-4px);
    }
  }

  &__vk {
    border-radius: 50%;
    position: absolute;
    padding: 12px;
    background-color: #0077ff;
    color: #fff;
    right: 16px;
    bottom: 16px;
    box-shadow: 0 4px 12px rgba(0, 119, 255, 0.5);
    cursor: pointer;
    transition: background-color 0.3s ease, box-shadow 0.3s ease;

    &.vk-animate {
      animation: vk-pulse 1.2s infinite;
      box-shadow: 0 0 20px 4px rgba(0, 119, 255, 0.7);
    }

    &:hover {
      background-color: #005bbb;
      box-shadow: 0 6px 20px rgba(0, 91, 187, 0.7);
    }
  }

  &__more {
    border-radius: 24px;
    position: absolute;
    background-color: #c43e3e; /* заменили цвет */
    padding: 10px 24px;
    color: #fff; /* лучше сделать текст белым для контраста */
    left: 16px;
    bottom: 16px;
    max-width: none;
    font-weight: 700;
    font-size: 1rem;
    box-shadow: 0 4px 12px rgba(196, 62, 62, 0.4); /* обновили тень под цвет */
    text-decoration: none;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    transition: background-color 0.3s ease, transform 0.3s ease;

    &:hover {
      background-color: #a73232; /* чуть темнее для ховера */
      color: #fff;
      transform: translateY(-2px) scale(1.05);
    }
  }
}

/* Анимация пульсации для кнопки VK */
@keyframes vk-pulse {
  0% {
    transform: scale(1);
    box-shadow: 0 0 8px 2px rgba(0, 119, 255, 0.6);
  }
  50% {
    transform: scale(1.1);
    box-shadow: 0 0 16px 6px rgba(0, 119, 255, 0.9);
  }
  100% {
    transform: scale(1);
    box-shadow: 0 0 8px 2px rgba(0, 119, 255, 0.6);
  }
}
</style>
