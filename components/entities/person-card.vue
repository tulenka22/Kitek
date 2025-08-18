<template>
  <div class="card">
    <div class="card__img">
      <img :src="`${instance.img}`" />
    </div>
    <div class="card__info">
      <p class="card__text">{{ instance.name }}</p>
      <p class="card__text card__text-w280"><b>Должность</b>: {{ instance.position }}</p>
      <p class="card__text">
        <b>Телефон</b>: <a :href="`tel:${instance.phone}`">{{ instance.phone }}</a>
      </p>
      <p class="card__text">
        <b>Email</b>: <a :href="`mailto:${instance.mail}`">{{ instance.mail }}</a>
      </p>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    instance: {
      type: Object,
    },
  },
}
</script>

<style scoped lang="scss">
.card {
  display: flex;
  align-items: center;
  &__img {
    width: 128px;
    height: 128px;
    border-radius: 50%;
    background-color: $grey-color;
    margin-right: 24px;
    flex: none;
    overflow: hidden;
  }
  &__text {
    margin-top: 4px;
    &-w280 {
      max-width: 280px;
    }
  }
  &__info {
    width: 280px;
  }
  @include medium-media {
    &__img {
      width: 64px;
      height: 64px;
    }
    &__text {
      font-size: 14px;
    }
    &__info {
      width: 250px;
    }
  }
}
</style>
