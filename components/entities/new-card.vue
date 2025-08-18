<template>
  <nuxt-link tag="button" :disabled="disabled" :to="`/news/${instance.id}`" class="card">
    <div class="card__info">
      <h2 class="card__title" v-safe-html="instance.title" />
      <h3 class="card__description" v-safe-html="instance.description" />
      <a class="card__link" v-if="instance.link" :href="instance.link">Подробнее</a>
    </div>
    <div class="card__preview">
      <IconWrapper width="210" height="210">
        <IconTangles />
      </IconWrapper>
      <div class="pruning">
        <img
          onerror="this.style.display = 'none'"
          class="card__img"
          :src="'/img/news/' + instance.id + '/preview.webp'"
          alt="preview" />
      </div>
    </div>
  </nuxt-link>
</template>

<script>
export default {
  name: 'EntitiesNewCard',
  props: {
    instance: {
      type: Object,
    },
    disabled: Boolean,
  },
}
</script>

<style scoped lang="scss">
.card {
  display: block;
  width: 100%;
  text-align: left;
  transition: $t box-shadow, $t border-color;
  padding: 24px;
  display: flex;
  box-shadow: $news-card-shadow;
  border-radius: $default-border-radius;
  border: 1px solid $border-color;
  background-color: $bg-control;
  position: relative;
  @include medium-media {
    overflow: hidden;
    max-height: 205px;
    &::after {
      content: '';
      position: absolute;
      bottom: 0;
      left: 0;
      display: block;
      height: 50px;
      width: 100%;
      background: linear-gradient(0deg, #fdfdfd 0%, rgba(253, 253, 253, 0) 100%);
    }
  }
  &:hover {
    box-shadow: $news-card-shadow-active;
    border-color: rgba($accent-color, 0.4);
  }
  &__info {
    user-select: none;
    flex-grow: 1;
  }
  &__title {
    @extend %tg-news-card-title;
    @include medium-media {
      font-size: 20px;
    }
  }
  &__description {
    min-height: 100px;
    max-width: 530px;
    margin-top: 12px;
    @extend %tg-news-card-description;
    @include medium-media {
      font-size: 14px;
    }
  }
  &__link {
    margin-top: 24px;
    color: $primary-color;
  }
  &__preview {
    @include medium-media {
      display: none;
    }
  }
  &__img {
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    position: absolute;
    width: 135px;
    height: auto;
    object-fit: cover;
    @include medium-media {
      display: none;
    }
  }
}
.pruning {
  position: relative;
  top: -172px;
  left: 38px;
  overflow: hidden;
  width: 135px;
  height: 135px;
  margin-bottom: -140px;
}
</style>
