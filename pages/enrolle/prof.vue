<template>
  <block-ab title="Профориентационная работа">
    <SplitLinks :links="links" />
    <p class="ab__subtitle" @click="block_video = !block_video">
      <icon-wrapper class="icon-tap" width="20" height="24"><icon-tapclick /></icon-wrapper>Видео
      мастер классы:
    </p>
    <ul v-show="block_video" class="ab__list" v-for="(video, videoIdx) of videos" :key="videoIdx">
      <li>
        <p class="ab__p">
          <b>{{ video.title }}</b>
        </p>
      </li>
      <iframe
        width="560"
        height="315"
        :src="video.link"
        title="YouTube video player"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        allowfullscreen></iframe>
    </ul>

    <common-documents-list json-path="documents/enrole-prof.json" />
  </block-ab>
</template>

<script>
import { createLink } from '~/core/helpers/link'
export default {
  data() {
    return {
      block_video: false,
      links: [
        createLink(
          'https://kafedra-po.irooo.ru/k2/itemlist/category/42-bpou-pedagogicheskij-kolledzh-1',
          'Профессиональные пробы "Колледж инновационных технологий, экономики и коммерции"'
        ),
        createLink('https://omsktec.ru/projects/ticket', 'Федеральный проект "Билет в будущее"'),
      ],
      videos: [
        {
          title: 'Арнольд Ю.А. Маслова Н.А. «Программирование фрагмента игры»',
          link: 'https://www.youtube.com/embed/Kw6r2kdl-S0',
        },
        {
          title: 'Аронова С.В. «Генерация бизнес идеи»',
          link: 'https://www.youtube.com/embed/BKKPA0obwug',
        },
        {
          title: 'Винокурова Н.А. «Экспресс методы обнаружения фальсификации товаров»',
          link: 'https://www.youtube.com/embed/GV9lhW82tGA',
        },
        {
          title:
            'Казакевич Е.А. «Виртуальный прием в клиентской службе отделения Пенсионного фонда России (ПФР)»',
          link: 'https://www.youtube.com/embed/HcZqFZtAEOw',
        },
        {
          title: 'Колиева М.А. «Изготовление оригами ошибори»',
          link: 'https://www.youtube.com/embed/HvyB5WT9_uI',
        },
        {
          title: 'Кузьменкина Н.А. «Сервировка новогоднего стола»',
          link: 'https://www.youtube.com/embed/g6nY4DYQhng',
        },
        {
          title:
            'Кукаркина С.М. «Разработка маршрутов и графиков доставки товаров автомобильным транспортом»',
          link: 'https://www.youtube.com/embed/qdRQslt96kY',
        },
        {
          title: 'Ли А.А. «Экспресс методы оценки качества потребительских товаров»',
          link: 'https://www.youtube.com/embed/gB25jdFj41M',
        },
        {
          title: 'Ли А.А. «Экспресс методы обнаружения фальсификации товаров»',
          link: 'https://www.youtube.com/embed/sfstGB0k4F0',
        },
        {
          title: 'Маслова Н.А. Смолиженко О.А. Создай коллаж «Ожившие картинки»',
          link: 'https://www.youtube.com/embed/KvQz9HeaH9E',
        },
        {
          title: 'Мастер класс «Изготовление декора для кондитерских изделий из вафельной бумаги»',
          link: 'https://www.youtube.com/embed/xokvK3ZzUjg',
        },
        {
          title:
            'Подольская Т.В. «Изготовление декора из мастики для оформления кондитерских изделий»',
          link: 'https://www.youtube.com/embed/VYtapqjVGrE',
        },
        {
          title: 'Понякшина М.В. «Оценка качества чая»',
          link: 'https://www.youtube.com/embed/ECNL3Wfg_QA',
        },
        {
          title: 'Речной транспорт сегодня',
          link: 'https://www.youtube.com/embed/VDqPG5wxiTQ',
        },
        {
          title: 'Степанова Г.В. «Оценка качества ювелирных изделий»',
          link: 'https://www.youtube.com/embed/J4L1FmdeI-8',
        },
        {
          title: 'Чикишева Т.В. «Составь свой баланс»',
          link: 'https://www.youtube.com/embed/PUkUPhFQU6s',
        },
        {
          title: 'Чукаева Л.И. «Организация доставки товаров автомобильным транспортом»',
          link: 'https://www.youtube.com/embed/ydw_GVs6fdE',
        },
        {
          title: 'Чукаева Л.И. «Применение визуального мерчендайзинга в оформлении витрины»',
          link: 'https://www.youtube.com/embed/Gjio_S_HF8g',
        },
        {
          title: 'Арнольд Ю.А. Маслова Н.А. «Программирование фрагмента игры»',
          link: 'https://www.youtube.com/embed/Kw6r2kdl-S0',
        },
        {
          title: 'Арнольд Ю.А. Маслова Н.А. «Программирование фрагмента игры»',
          link: 'https://www.youtube.com/embed/Kw6r2kdl-S0',
        },
        {
          title: 'Арнольд Ю.А. Маслова Н.А. «Программирование фрагмента игры»',
          link: 'https://www.youtube.com/embed/Kw6r2kdl-S0',
        },
        {
          title: 'Арнольд Ю.А. Маслова Н.А. «Программирование фрагмента игры»',
          link: 'https://www.youtube.com/embed/Kw6r2kdl-S0',
        },
      ],
    }
  },
}
</script>

<style scoped lang="scss">
.ab {
  &__link {
    color: $accent-color;
  }
}
</style>
