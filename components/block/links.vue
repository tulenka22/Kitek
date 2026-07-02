<template>
  <div class="links">
    <AppBlock title="Полезные ссылки">
      <template #content>
        <SplitLinks :links="links" :gos="true" :support="true" />

        <!-- Баннер после ссылок -->
        <div class="imgblock">
          <a href="https://finombudsman.ru/" target="_blank">
            <img
              class="help help--desktop"
              src="/img/banner-sfu-2000x1000.png"
              alt="Ссылка на проект «Победа» ОНФ"
            />
            <img
              class="help help--mobile"
              src="/img/banner-sfu-2000x1000.png"
              alt="Ссылка на проект «Победа» ОНФ"
            />
          </a>
        </div>
      </template>
    </AppBlock>
  </div>
</template>

<script>
import { links } from '~/core/lists'
export default {
  name: 'BlockLinks',
  data() {
    return {
      links,
    }
  },
}
</script>

<style scoped lang="scss">
.links {
  margin-top: 60px;

  &__group {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-wrap: wrap;
  }

  &__icon {
    width: 300px;
    height: 180px;
    object-fit: contain;
    margin-right: 16px;

    @include medium-media {
      width: 180px;
      height: 120px;
    }
  }

  &__img {
    width: 1084px;
    height: 222px;
    margin: 0 auto;
    margin-top: 48px;
  }
}

/* Стили для баннера */
.imgblock {
  display: block;
  width: 100%;

  margin-bottom: 10px;
  text-align: center;
}

.help {
  max-width: 100%;
  height: auto;
  border: 0;
}

.help--desktop {
  display: block;
  max-height: 21vw;
  margin: 0 auto;

  @media screen and (max-width: 640px) {
    display: none;
  }
}

.help--mobile {
  display: none;

  @media screen and (max-width: 640px) {
    display: block;
    max-width: 240px;
    max-height: 400px;
    margin: 0 auto;
  }
}
</style>
