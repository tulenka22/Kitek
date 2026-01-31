<!-- <template>
  <AppBlock
    :content-style="{
      padding: '24px',
    }"
    class="events__self testgipn"
    title="2025 ГОД ЗАЩИТНИКА ОТЕЧЕСТВА">
    <div class="left">
      <swiper :options="swiperOptions">
        <swiper-slide
          ><a href="https://omsktec.ru/enrolle/enrolle-menu"
            ><img
              style="width: auto; height: auto"
              class="event__img-main"
              alt="Events-Image"
              loading="preload"
              src="/img/organization/Bannerpobeda.webp" /> </a
        ></swiper-slide>
      </swiper>
    </div>
  </AppBlock>
</template>

<script>
export default {
  name: 'BannerMain',
}
</script>

<style scoped lang="scss">
.events__self {
  margin-bottom: 20px;
}
</style> -->

<template>
  <AppBlock
    :content-style="{
      padding: '24px',
    }"
    class="events__self"
    title="2026 ГОД ЕДИНСТВА НАРОДОВ РОССИИ">
    <div class="left">
      <swiper :options="swiperOptions">
        <swiper-slide>
          <a href="https://omsktec.ru/enrolle/enrolle-menu">
            <!-- Изображение для десктопов (отображается на больших экранах) -->
            <img
              class="event__img-main event__img-desktop"
              alt="Events-Image Desktop"
              loading="lazy"
              src="/img/organization/GENR_2026_v4.webp" />
            <!-- Изображение для мобильных устройств (отображается на маленьких экранах) -->
            <img
              class="event__img-main event__img-mobile"
              alt="Events-Image Mobile"
              loading="lazy"
              src="/img/organization/GENR_2026_v1.webp" />
          </a>
        </swiper-slide>
      </swiper>
    </div>
  </AppBlock>
</template>

<script>
export default {
  name: 'BannerMain',
}
</script>

<style scoped lang="scss">
.events__self {
  margin-bottom: 20px;
}

.event__img-main {
  width: 100%;
  height: auto;
  display: block;
}

.event__img-mobile {
  display: none;
}

.event__img-desktop {
  display: block;
}

@media (max-width: 768px) {
  .event__img-desktop {
    display: none;
  }

  .event__img-mobile {
    display: block;
  }
}

@media (max-width: 480px) {
  .event__img-mobile {
    width: 100%;
    height: auto;
  }
}
</style>
