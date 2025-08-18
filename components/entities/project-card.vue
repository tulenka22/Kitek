<template>
  <nuxt-link class="card" :to="instance.link">
    <h2 class="card__title">{{ instance.title }}</h2>
    <div class="card__content">
      <p class="card__description" v-safe-html="instance.description" />
      <span class="card__spacer" />
      <img
        :alt="`Project-${instance.title}`"
        :src="instance.img"
        :style="instance.imgStyle"
        class="card__img"
        loading="lazy" />
    </div>
    <svg class="waves" viewBox="0 0 620 421" fill="none" xmlns="http://www.w3.org/2000/svg">
      <g clip-path="url(#clip0_347_36)">
        <g filter="url(#filter0_d_347_36)">
          <path
            d="M44 420.5C84 380 99.6216 343.052 188.5 312.5C220.5 301.5 237.131 248.704 278 240C332 228.5 326.5 169 364 151.5C443.291 114.498 411 92.5 464.5 83.5C518 74.5 569.5 39.5 620 2.5V420.5H44Z"
            fill="#FAFAFA" />
        </g>
        <g filter="url(#filter1_d_347_36)">
          <path
            d="M92 421C132 380.5 131 338.5 207 310C240.708 297.36 270.131 223.704 311 215C365 203.5 358 148.5 395.5 131C474.791 93.9975 471 80 488.5 54.5C506 29 590.5 40 641 3V421H92Z"
            fill="#FAFAFA" />
        </g>
        <g filter="url(#filter2_d_347_36)">
          <path
            d="M121 421C158.887 382.632 141.316 370.444 225.5 341.5C255.81 331.079 266.29 274.745 305 266.5C356.148 255.605 360.481 171.579 396 155C471.103 119.945 464.324 96.8947 506 77C547.676 57.1053 593.168 60.0526 641 25V421H121Z"
            fill="#FAFAFA" />
        </g>
      </g>
      <defs>
        <filter
          id="filter0_d_347_36"
          x="4"
          y="-38.5"
          width="656"
          height="498"
          filterUnits="userSpaceOnUse"
          color-interpolation-filters="sRGB">
          <feFlood flood-opacity="0" result="BackgroundImageFix" />
          <feColorMatrix
            in="SourceAlpha"
            type="matrix"
            values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0"
            result="hardAlpha" />
          <feOffset dy="-1" />
          <feGaussianBlur stdDeviation="20" />
          <feComposite in2="hardAlpha" operator="out" />
          <feColorMatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.05 0" />
          <feBlend mode="normal" in2="BackgroundImageFix" result="effect1_dropShadow_347_36" />
          <feBlend
            mode="normal"
            in="SourceGraphic"
            in2="effect1_dropShadow_347_36"
            result="shape" />
        </filter>
        <filter
          id="filter1_d_347_36"
          x="52"
          y="-38"
          width="629"
          height="498"
          filterUnits="userSpaceOnUse"
          color-interpolation-filters="sRGB">
          <feFlood flood-opacity="0" result="BackgroundImageFix" />
          <feColorMatrix
            in="SourceAlpha"
            type="matrix"
            values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0"
            result="hardAlpha" />
          <feOffset dy="-1" />
          <feGaussianBlur stdDeviation="20" />
          <feComposite in2="hardAlpha" operator="out" />
          <feColorMatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.05 0" />
          <feBlend mode="normal" in2="BackgroundImageFix" result="effect1_dropShadow_347_36" />
          <feBlend
            mode="normal"
            in="SourceGraphic"
            in2="effect1_dropShadow_347_36"
            result="shape" />
        </filter>
        <filter
          id="filter2_d_347_36"
          x="81"
          y="-16"
          width="600"
          height="476"
          filterUnits="userSpaceOnUse"
          color-interpolation-filters="sRGB">
          <feFlood flood-opacity="0" result="BackgroundImageFix" />
          <feColorMatrix
            in="SourceAlpha"
            type="matrix"
            values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0"
            result="hardAlpha" />
          <feOffset dy="-1" />
          <feGaussianBlur stdDeviation="20" />
          <feComposite in2="hardAlpha" operator="out" />
          <feColorMatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.05 0" />
          <feBlend mode="normal" in2="BackgroundImageFix" result="effect1_dropShadow_347_36" />
          <feBlend
            mode="normal"
            in="SourceGraphic"
            in2="effect1_dropShadow_347_36"
            result="shape" />
        </filter>
        <clipPath id="clip0_347_36">
          <rect width="620" height="421" fill="white" />
        </clipPath>
      </defs>
    </svg>
  </nuxt-link>
</template>

<script>
export default {
  name: 'EntitiesProjectCard',
  props: {
    instance: {
      type: Object,
    },
  },
}
</script>

<style scoped lang="scss">
.card {
  transition: $t border-color;
  padding: 16px;
  background-color: $bg-control;
  border-radius: $default-border-radius;
  position: relative;
  min-height: 200px;
  overflow: hidden;
  box-shadow: $special-shadow;
  border: 1px solid $border-color;
  user-select: none;
  display: block;

  backface-visibility: hidden;
  &:hover {
    border-color: rgba($accent-color, 0.6);
  }
  &__title {
    @include tg(19px, 500, 18px, normal, 'Montserrat');
  }
  &__description {
    margin-top: 12px;
    @include tg(14px, 400, 16px, 0.6px);
  }
  &__img {
    position: absolute;
    right: 0;
    bottom: 0;
    object-fit: contain;
    opacity: 0.4;
    z-index: 10;
    color: $primary-text-color;
  }
  &__content {
    display: flex;
  }
  &__spacer {
    width: 140px;
    justify-self: flex-end;
  }
}

.waves {
  position: absolute;
  right: -4px;
  top: 4px;
  opacity: 0.9;
  width: 275px;
  height: 200px;
  @include medium-media {
    width: 240px;
    height: 150px;
    bottom: 0;
    top: unset;
  }
  // z-index: 0;
}
</style>
