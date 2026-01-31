<template>
  <block-ab title="Билет в будущее">
    <EntitiesImgScreen :instance="visibleAwards" :images="awards" :separatePage="false" />
    <img alt="Логотип билет в будущие" src="/img/educational/Logo-BvB.webp" class="ab__img" />
    <p class="ab__p">
      Колледж стал площадкой для проведения практических мероприятий в рамках федерального проекта
      по ранней профессиональной ориентации учащихся 6-11-х классов общеобразовательных организаций
      «Билет в будущее» в 2022 году.
    </p>
    <p class="ab__p">
      Проект по ранней профессиональной ориентации учащихся 6-11 классов общеобразовательных
      организаций «Билет в будущее» решает задачу повышения осознанности школьников в выборе
      профессии. В рамках проекта школьники участвуют в профессиональных пробах, где имеют
      возможность на практике попробовать свои силы в интересных для себя профессиях: визуальный
      мерчандайзер, программист, повар-кондитер и предприниматель малого бизнеса.
    </p>
    <p class="ab__p">
      В рамках практических мероприятий высока роль наставника – именно он знакомит подростка с
      основной информацией о профессиональной области, под его руководством участник выполняет
      заданную рабочую операцию, получает оценку результата и обратную связь с рекомендациями по
      развитию. Выделяется три возрастных категории участников: 6-7, 8-9 и 10-11 классы.
    </p>
    <p class="ab__p">
      В ходе профессиональной пробы участники решают одну или несколько практических задач и
      выполняют реальные рабочие операции, относящиеся к конкретной профессиональной области. Проба
      подразумевает работу участников с материалами, инструментами, оборудованием, программным
      обеспечением, без игровой адаптации и в условиях, максимально приближенных к реальным.
    </p>
    <p class="ab__p">
      В ходе пробы участники взаимодействуют с наставником, являющимся носителем профессиональных
      компетенций, получая от него теоретические знания, практические рекомендации, обратную связь и
      оценку по итогам пробы.
    </p>

    <p class="ab__p">
      <b>Координатор площадки: Юрьева Елена Георгиевна</b>
      <a href="tel:8(3812) 68-07-82"> т. 8(3812) 68-07-82,</a> <b> e-mail:</b>
      <a href="mailto:tradeconomy@mail.ru">tradeconomy@mail.ru </a>
    </p>
    <h2 class="ab__subtitle">Наставники:</h2>
    <p class="ab__p">
      <b>Профессиональное направление: "Повар, кондитер" (Комфортная среда):</b>
    </p>
    <ul class="ab__list">
      <li>Федорова Галина Николаевна</li>
      <li>Подольская Тамара Васильевна</li>
      <li>Кузьменкина Наталья Александровна</li>
    </ul>
    <p class="ab__p">
      <b>Профессиональное направление: "Предприниматель малого бизнеса" (Деловая среда): </b>
    </p>
    <ul class="ab__list">
      <li>Покутная Виктория Александровна</li>
      <li>Спирина Наталья Алексеевна</li>
      <li>Аронова Светлана Владимировна</li>
    </ul>
    <p class="ab__p">
      <b>Профессиональное направление: "Товаровед-эксперт" (Деловая среда): </b>
    </p>
    <ul class="ab__list">
      <li>Ли Анна Амуровна</li>
      <li>Степанова Галина Васильевна</li>
    </ul>
    <p class="ab__p">
      <b>Профессиональное направление: "Программист" (Умная среда): </b>
    </p>
    <ul class="ab__list">
      <li>Орлова Вера Михайловна</li>
    </ul>
    <p class="ab__p">
      <b
        >Профессиональное направление: "Разработчик Web и мультимедийных приложений" (Умная среда):
      </b>
    </p>
    <ul class="ab__list">
      <li>Арнольд Юлия Алексеевна</li>
      <li>Маслова Надежда Алексеевна</li>
      <li>Смолиженко Ольга Александровна</li>
    </ul>
    <p class="ab__p">
      <b>Профессиональное направление: "Визуальный мерчандайзер" (Креативная среда): </b>
    </p>
    <ul class="ab__list">
      <li>Чукаева Людмила Ивановна</li>
    </ul>
    <p class="ab__p">
      <b>Профессиональное направление: "Официант" (Социальная среда):</b>
    </p>
    <ul class="ab__list">
      <li>Севернюк Ирина Александровна</li>
    </ul>
    <p class="ab__p">
      <b
        >Профессиональное направление: "Специалист по гостеприимству: администратор отеля"
        (Социальная среда):
      </b>
    </p>
    <ul class="ab__list">
      <li>Колиева Марина Александровна</li>
    </ul>
    <p class="ab__p">
      <b>Профессиональное направление: "Фронтенд-разработчик" (Умная среда): </b>
    </p>
    <ul class="ab__list">
      <li>Кутиков Павел Алексеевич</li>
    </ul>
    <p class="ab__p">
      <b>Профессиональное направление: "Бухгалтерский учет" (Деловая среда): </b>
    </p>
    <ul class="ab__list">
      <li>Кудинова Олеся Викторовна</li>
    </ul>
    <swiper class="slider_committe" :options="opts">
      <swiper-slide v-for="(link, imgIdx) of img" :key="imgIdx">
        <img class="img-single__minimg" alt="Slider-Image" :src="link" />
      </swiper-slide>
    </swiper>
    <common-documents-list json-path="documents/project-ticket.json" />
    <!-- <p class="ab__p"><b>Благодарности:</b></p> -->
    <swiper class="slider_committe" :options="opts">
      <swiper-slide v-for="(link, imgIdx) of awards" :key="imgIdx">
        <img
          class="img-single__minimg"
          alt="Slider-Image"
          :src="link"
          v-on:click="visibleAwards = !visibleAwards" />
      </swiper-slide>
    </swiper>
    <!-- <h2 class="ab__subtitle">Новости:</h2>
    <div class="news">
      <EntitiesNewCard
        v-for="(n, nIdx) of news"
        :key="nIdx"
        :instance="n"
        v-if="n.teg == 'ticket'" />
    </div> -->
  </block-ab>
</template>

<script>
import { loadDynamic } from '~/core/helpers/file'
export default {
  async created() {
    try {
      this.news = JSON.parse(await loadDynamic('dynamic/news/news.json'))
    } catch {
      console.log('Проверьте валидность JSON новостей и событий!')
    }
  },
  data() {
    return {
      news: [],
      img: [
        '/img/projects/ticket/bvb1.jpg',
        '/img/projects/ticket/bvb2.jpg',
        '/img/projects/ticket/bvb3.jpg',
        '/img/projects/ticket/bvb4.jpg',
        '/img/projects/ticket/bvb5.jpg',
        '/img/projects/ticket/bvb6.jpg',
        '/img/projects/ticket/bvb7.jpg',
        '/img/projects/ticket/bvb8.jpg',
        '/img/projects/ticket/bvb9.jpg',
        '/img/projects/ticket/bvb10.jpg',
        '/img/projects/ticket/bvb11.jpg',
        '/img/projects/ticket/bvb12.jpg',
      ],
      awards: ['/img/projects/ticket/award1.jpg'],
      visibleAwards: false,
      opts: {
        autoplay: {
          enabled: true,
          delay: 3000,
        },
      },
    }
  },
}
</script>

<style scoped lang="scss">
.ab {
  &__img {
    position: absolute;
    height: 200px;
    width: 200px;
    right: 24px;
    top: 24px;
    @include high-medium-media() {
      width: 150px;
      height: 150px;
      right: 12px;
      top: 10px;
      opacity: 0.4;
    }
  }
}
.slider_committe {
  cursor: pointer;
  margin: 0px;
  margin-top: 24px;
  max-width: 1000px;
}
</style>
