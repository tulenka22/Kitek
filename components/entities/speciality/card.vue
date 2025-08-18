<template>
  <nuxt-link class="card" :to="`/specialties/${preparedCode}`">
    <div class="card__info">
      <h2 class="card__title">{{ instance.title }}</h2>
      <div class="card__code">
        <p class="card__code__self">Код: {{ instance.code }}</p>
        <p class="card__podrob">Подробнее</p>
      </div>
    </div>
    <CommonButton class="card__btn"> Выбрать </CommonButton>
  </nuxt-link>
</template>

<script>
export default {
  name: 'EntitiesSpecialityCard',
  props: {
    instance: {
      type: Object,
    },
  },
  computed: {
    preparedCode() {
      if (this.instance.internalCode) return this.instance.internalCode
      return this.instance.code.replaceAll('.', '')
    },
  },
}
</script>

<style scoped lang="scss">
.card {
  padding: 32px;
  display: flex;
  align-items: center;
  position: relative;
  border-radius: $default-border-radius;
  border: 1px solid $border-color;
  @include medium-media {
    padding: 16px;
    display: block;
    box-shadow: $special-shadow;
  }
  &__info {
    flex-grow: 1;
    user-select: none;
  }
  &__title {
    @include tg(20px, 400, 26px, 2px);
    max-width: 900px;
    @include medium-media {
      @include tg(15px, 400, 22px, 1px);
    }
  }
  &__code {
    font-family: Montserrat;
    display: flex;
    align-items: center;
    margin-top: 8px;
    font-size: 13px;
    @include medium-media {
      margin-top: 12px;
    }
    &__self {
      flex-grow: 1;
      color: $nav-link;
    }
  }
  &__btn {
    @include medium-media {
      display: none;
    }
  }
  &__podrob {
    display: none;
    color: $accent-color;
    text-decoration: underline;
    text-underline-offset: 3px;
    @include medium-media {
      display: block;
    }
  }
}
</style>
