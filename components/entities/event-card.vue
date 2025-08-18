<template>
  <a :href="instance.link" class="card">
    <div class="card__info">
      <h2 class="card__title" v-safe-html="instance.title" />
      <h3 class="card__subtitle" v-safe-html="instance.subtitle" />
    </div>
    <div class="card__icon" v-if="instance.icon">
      <component :is="`Icon${instance.icon}`" />
    </div>
  </a>
</template>

<script>
export default {
  name: 'EntitiesEventCard',
  props: {
    instance: {
      type: Object,
    },
  },
}
</script>

<style scoped lang="scss">
.card {
  transition: $t box-shadow, $t border-color;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-radius: $default-border-radius;
  border: 1px solid $border-color;
  padding: 16px;
  box-shadow: $news-card-shadow;
  background-color: $bg-control;
  &:hover {
    box-shadow: $news-card-shadow-active;
    border-color: rgba($accent-color, 0.4);
  }
  &__info {
    user-select: none;
  }
  &__title {
    color: $primary-color;
    @extend %tg-news-card-title;
  }
  &__subtitle {
    color: $nav-link;
    margin-top: 2px;
    @extend %tg-event-card-subtitle;
  }
  &__icon {
    color: $accent-color;
  }
}
</style>
