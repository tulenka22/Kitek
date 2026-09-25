<template>
  <div class="events">
    <div>
      <AppBlock
        :content-style="{
          padding: '0',
          color: 'white',
          overflow: 'hidden',
          position: 'relative',
          borderRadius: '10px',
        }"
        class="kitek-promo-block"
        title="Единый день открытых дверей">
        
        <!-- Контейнер для картинки -->
        <div class="banner-image-container">
          <img 
            src="@/static/img/banner.png" 
            alt="Единый день открытых дверей — 17 октября 2026 г. в 10:00" 
            class="banner-image"
          />
        </div>

      </AppBlock>
    </div>
  </div>
</template>

<script>
export default {
  name: 'OpenDoorBanner',
}
</script>

<style scoped lang="scss">
.kitek-promo-block {
  // Убираем лишние тени и границы, чтобы картинка смотрелась как единое целое
  border: none !important;
  box-shadow: none !important;
  background: transparent !important;
}

.banner-image-container {
  width: 100%;
  height: auto;
  display: block;
  line-height: 0; // Убирает нежелательный отступ снизу под картинкой
}

.banner-image {
  width: 100%;
  height: auto;
  display: block;
  object-fit: contain; // Картинка не обрезается, а вписывается полностью
}

// Для мобильных устройств
@media (max-width: 768px) {
  .banner-image {
    // Если нужно, чтобы картинка занимала всю высоту экрана — раскомментируйте:
    // min-height: 100vh;
    // object-fit: cover;
  }
}
</style>