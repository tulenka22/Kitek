<template>
  <div class="block__wrapper">
    <div class="block" :style="blockStyle">
      <header class="block__header">
        <h1 class="block__title">
          {{ title }}
        </h1>
        <slot name="header" />
      </header>
      <slot name="content">
        <main v-if="!withoutBody" :style="contentStyle" class="block__content">
          <slot />
        </main>
      </slot>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AppBlock',
  props: {
    title: {
      type: String,
    },
    blockStyle: {
      type: Object,
    },
    contentStyle: {
      type: Object,
    },
    withoutBody: {
      type: Boolean,
    },
  },
}
</script>

<style scoped lang="scss">
.block {
  @include scrollbar;
  padding: 0 0 0 0;
  &__wrapper {
    border-radius: $default-border-radius;
    box-shadow: $control-shadow;
    overflow: hidden;
    @include medium-media {
      // border-radius: 0;
    }
  }
  &__header {
    transition: $t background-color;
    position: sticky;
    top: 0;
    z-index: 1000;

    display: flex;
    align-items: center;

    padding: 16px 0;
    background-color: #fdfdfdfb;
    box-shadow: $nav-drop-shadow;

    user-select: none;

    // Полоска справа от заголовка
    &::before {
      content: '';
      display: block;
      width: 10px;
      height: 60%;
      position: absolute;
      left: 0;
      background-color: $primary-color;
      border-radius: 40px;
      @include medium-media {
        width: 8px;
      }
    }
  }
  &__title {
    margin-left: 28px;
    color: $primary-color;
    @extend %tg-block-title;
    @include medium-media {
      @include tg(21px, 600, 21px, normal, 'Montserrat');
    }
  }
  &__content {
    padding: 48px;
    &::v-deep .card {
      margin-bottom: 16px;
      &:last-child {
        margin-bottom: 0;
      }
    }
  }
}
</style>
