<template>
  <block-ab
    title="Видеоматериалы по правовому просвещению, разработанных Генеральной прокуратурой России">
    <div class="video-layout">
      <!-- Горизонтальное видео -->
      <div class="video-box landscape">
        <!-- controls - включает пульт, playsinline - для мобильных -->
        <video controls playsinline preload="auto" class="video-player">
          <source src="/video/odna.mp4" type="video/mp4" />
          Ваш браузер не поддерживает тег video.
        </video>
      </div>

      <!-- Вертикальное видео -->
      <div class="video-box portrait">
        <div class="portrait-badge">Shorts</div>
        <video controls playsinline preload="auto" class="video-player">
          <source src="/video/onlinelovushka.mp4" type="video/mp4" />
          Ваш браузер не поддерживает тег video.
        </video>
      </div>
    </div>
  </block-ab>
</template>

<style scoped lang="scss">
.video-layout {
  display: flex;
  gap: 20px;
  align-items: flex-start;
  padding: 20px 0;

  @media (max-width: 900px) {
    flex-direction: column;
    align-items: center;
  }
}

.video-box {
  background: #000;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
  width: 100%; // Для адаптивности
}

.landscape {
  flex: 2;
  aspect-ratio: 16 / 9;
}

.portrait {
  flex: 0.8;
  max-width: 300px;
  aspect-ratio: 9 / 16;
  position: relative;
}

.video-player {
  width: 100%;
  height: 100%;
  display: block;
  object-fit: contain; // Видео не будет обрезаться
}

.portrait-badge {
  position: absolute;
  top: 10px;
  right: 10px;
  background: red;
  color: white;
  padding: 2px 8px;
  border-radius: 4px;
  font-size: 10px;
  z-index: 10;
}
</style>
