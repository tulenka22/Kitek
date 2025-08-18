<template>
  <block-ab title="«Скетчбук СПО»">
    <EntitiesImgScreen :instance="visible" :images="imagesContests" :separatePage="false" />
    <SplitLinks :links="links" />
    <p class="ab__p" @click=";(kk = !kk), (visible = false)">
      <icon-wrapper class="icon-tap" width="20" height="24"><icon-tapclick /></icon-wrapper
      ><b>"КОНКУРСЫ ПРОФЕССИОНАЛЬНОГО МАСТЕРСТВА"</b>
    </p>
    <div v-show="kk">
      <block-ab title="«Студенческая жизнь: открывай мир, твори будущее!»">
        <div class="ab__video">
          <p class="ab__p">
            Уважаемые студенты! В процессе получения знаний будущей специальности/профессии всегда
            найдётся время для новых открытий! В нашем колледже у вас всегда есть возможность
            реализовать свои творческие способности, принять участие в конкурсах, фестивалях,
            культурных мероприятиях.
          </p>
          <p class="ab__p">
            В течении многих лет студенты нашего колледжа принимают участие и отмечены наградами
            высших степеней во Всероссийских, региональных и городских конкурсах и фестивалях.
            Кульминация творческих конкурсов - Фестиваль «Российская студенческая весна» отмечена
            результатами в номинациях «Вокальное направление», «Театральное направление»,
            «Инструментальное направление», «Оригинальный жанр».
          </p>
          <p class="ab__p">
            Откройте миру свои таланты в музыке, пении, художественном чтении, театральных
            постановках, сочиняйте свои истории в литературе, на сцене и в жизни! Принимайте участие
            в праздничных программах, творческих проектах колледжа в течение года!
          </p>
          <p class="ab__p">Для вас работают коллективы:</p>
          <p class="ab__p">
            - Вокальный коллектив «Романтики» - педагог Ольга Владимировна Медведева
          </p>
          <p class="ab__p">
            - Любительское театральное объединение «Прометей» - педагог Никифорова Татьяна Петровна
          </p>
          <p class="ab__p">- «Имидж- школа ведущих» - педагог Никифорова Татьяна Петровна</p>
          <p class="ab__p">
            Желающие могут записаться у руководителей в актовом зале корпуса 1 ул.27-я северная 69.
          </p>
          <div class="img-container">
            <img class="img-single__minimg" src="/img/sketchbook/1/preview.webp" />
          </div>
          <p class="ab__p">
            В колледже успешно развивается волонтерское движение Во всех корпусах созданы отряды
            волонтеров , работающие по следующим направлениям: профилактика вредных зависимостей
            среди студентов колледжа, оказание помощи при проведении различных мероприятий в
            колледже, участие в социально-благотворительных акциях: «Щедрый вторник»,
            «Рождественская звезда», «Подарок в каждый дом», «Подарок за спасибо», «День с
            ветераном», «Поможем нашим детям», «Помощь нашим меньшим братьям» и др. отряд «Позитив"
            руководитель Речкина Е. В. 2- 3 корпус отряд «Добродел» руководитель Смирнова Л.П., 1
            корпус отряд «Алые паруса» руководитель Янюшкина Е.Н. 4 корпус
          </p>
          <p class="ab__p">
            Мы ждём активных первокурсников для вступления в волонтерское движение! Пополни наши
            ряды - стань волонтёром
          </p>
          <div class="img-container">
            <img class="img-single__minimg" src="/img/sketchbook/1/1.webp" />
          </div>
        </div>
        <br />
        <br />
        <p class="ab__p click ab__link">
          <b red-prim
            ><icon-wrapper class="icon-tap" width="20" height="24"><icon-tapclick /></icon-wrapper
            ><a href="https://www.omsktec.ru/student/sportclub"
              >Студенческий спортивный клуб "Старт"</a
            ></b
          >
        </p>
      </block-ab>
    </div>

    <p class="ab__p" @click=";(om = !om), (visible = false)">
      <icon-wrapper class="icon-tap" width="20" height="24"><icon-tapclick /></icon-wrapper
      ><b>Предприятия-работодатели колледжа</b>
    </p>
    <div v-show="om">
      <p class="ab__p otstyp__p" @click=";(om11 = !om11), (visible = false)">
        <icon-wrapper class="icon-tap" width="20" height="24"><icon-tapclick /></icon-wrapper
        ><b>ООО ''Коммерчерская компания ОМСК''</b>
      </p>
      <div v-show="om11">
        <block-ab title="ООО ''Коммерчерская компания ОМСК''">
          <p class="ab__p">
            ООО "Коммерческая компания "Омск" является одним из участников-партнеров
            образовательного кластера СПО «Союз+» в отрасли «Туризм и сфера услуг», что предполагает
            совместную деятельность по реализации образовательных программ ФП «Профессионалитет» для
            подготовки востребованных кадров в регионе.
          </p>
          <p class="ab__p">
            Ресторан "Клуб деловых людей" - это профессиональная организация мероприятий любого
            уровня! Более 30 лет ресторан славится своим гостеприимством и радушными приёмами. Так
            же за эти годы накоплен опыт по обслуживанию выездных мероприятий различного уровня.
            Находится ресторан по адресу Яковлева, 143.
          </p>
          <p class="ab__p">
            В ресторане можно найти разнообразное меню и оригинальные авторские рецепты,
            великолепную технику приготовления и отличную подачу блюд. В меню есть русская,
            европейская и восточная кухня. Русская кухня особенно славится обилием разнообразных
            закусок, она богата интересными рецептами и разнообразием сочетания вкусов. В ресторане
            "Клуб деловых людей" работают настоящие профессионалы! В нашем ресторане 5 банкетных
            залов. Роскошный интерьер, художественные фрески, сверкающая роскошь люстр и современное
            оборудование создадут неповторимую, удивительную атмосферу праздника.
          </p>
          <p class="ab__p">
            Залы оформлены с подлинно королевской роскошью и отлично подойдут, как для желающих
            устроить великолепный свадебный банкет, так и для проведения незабываемых выпускных
            вечеров, юбилейных торжеств и корпоративных мероприятий. Ресторан "Клуб деловых людей"
            организует выездные мероприятия любой сложности, есть возможность организовать кейтеринг
            до 1500 персон.
          </p>
          <p class="ab__p">
            Обучающиеся колледжа приходят к нам сначала на экскурсии, потом на производственную
            практику и остаются работать. Производственная практика позволяет в полной мере ощутить
            и осознать специфику будущей профессии. В процессе работы формируются навыки
            использования теоретических знаний в практической деятельности, умение применять
            оптимальные решения в конкретных ситуациях, осуществить объективную оценку собственных
            профессиональных качеств. Она позволяет окончательно убедиться в правильности выбранной
            профессии, сформировать свое независимое мнение о специальности, а также спланировать
            свою дальнейшую деятельность. Во время практики, обучающиеся КИТЭК не только приобретают
            полезные для себя навыки, но становятся незаменимыми помощниками персоналу.
          </p>
          <p class="ab__p">
            Студентов в нашем ресторане воспринимают как новых коллег. К процессу мы подходим как к
            адаптации новых сотрудников под кураторством более опытных наставников. Наши вчерашние
            практиканты действительно становятся потом штатными сотрудниками, успешно работают в
            ресторане. Кроме того, мы убеждены: только практический опыт работы в ресторане поможет
            студенту лучше усвоить теорию. Молодой человек скажет: «Всё это я проходил сам, на
            собственном опыте».
          </p>
          <p class="ab__p">
            Мы будем рады, что именно вы станете частью нашей большой и дружной команды!
          </p>
          <div class="img-container">
            <img class="img-single__minimg" src="/img/sketchbook/2/preview.webp" />
            <img class="img-single__minimg" src="/img/sketchbook/2/1.webp" />
          </div>
          <div class="img-container">
            <img class="img-single__minimg" src="/img/sketchbook/2/2.webp" />
            <img class="img-single__minimg" src="/img/sketchbook/2/3.webp" />
          </div>
        </block-ab>
      </div>

      <p class="ab__p otstyp__p">
        <icon-wrapper class="icon-tap" width="20" height="24"><icon-tapclick /></icon-wrapper
        ><b> <a href="/data/sketchbook/Гостиница-Ибис-Сибирь.pdf">Гостиница Ибис Сибирь</a></b>
      </p>
      <p class="ab__p otstyp__p">
        <icon-wrapper class="icon-tap" width="20" height="24"><icon-tapclick /></icon-wrapper
        ><b> <a href="/data/sketchbook/Стройподряд.pdf">Стройподряд</a></b>
      </p>

      <!--
      <p class="ab__p otstyp__p" @click=";(om = !om), (visible = false)">
        <icon-wrapper class="icon-tap" width="20" height="24"><icon-tapclick /></icon-wrapper
        ><b>1.2</b>
      </p>
      <div v-show="om"></div>
    --></div>

    <p class="ab__p">
      <icon-wrapper class="icon-tap" width="20" height="24"><icon-tapclick /></icon-wrapper
      ><b>
        <a href="/data/sketchbook/Восстребованность_специальностей_колледжа.pdf"
          >Востребованность профессий и специальностей колледжа</a
        ></b
      >
    </p>

    <p class="ab__p" @click=";(vume = !vume), (visible = false)">
      <icon-wrapper class="icon-tap" width="20" height="24"><icon-tapclick /></icon-wrapper
      ><b>Расскажем о наших педагогах</b>
    </p>
    <div v-show="vume">
      <p class="ab__p otstyp__p">
        <icon-wrapper class="icon-tap" width="20" height="24"><icon-tapclick /></icon-wrapper
        ><b>
          <a href="https://www.omsktec.ru/news/492"
            >В предверии дня СПО мы запускаем серию видеороликов</a
          ></b
        >
      </p>
    </div>

    <p class="ab__p" @click=";(student = !student), (visible = false)">
      <icon-wrapper class="icon-tap" width="20" height="24"><icon-tapclick /></icon-wrapper
      ><b>Наши выпускники – наша гордость!</b>
    </p>
    <div v-show="student">
      <p class="ab__p otstyp__p">
        <icon-wrapper class="icon-tap" width="20" height="24"><icon-tapclick /></icon-wrapper>
        <video class="ab__video" controls>
          <source src="/video/detskoe.mp4" type="video/mp4" />
          Ваш браузер не поддерживает видео
        </video>
        <video class="ab__video" controls>
          <source src="/video/konditerka.mp4" type="video/mp4" />
          Ваш браузер не поддерживает видео
        </video>
        <video class="ab__video" controls>
          <source src="/video/viktoria.mp4" type="video/mp4" />
          Ваш браузер не поддерживает видео
        </video>
      </p>
    </div>
  </block-ab>
</template>

<script>
import { createLink } from '~/core/helpers/link'
export default {
  data() {
    return {
      student: false,
      vume: false,
      om33: false,
      om22: false,
      om11: false,
      om: false,
      kk: false,
      general_education: false,
      professional_education: false,
      thematic_olympiads: false,
      photo_exhibition: false,
      visible: false,
      visiblev: false,
      visiblek: false,
      imagesContests: [
        '/img/contests/w1.jpg',
        '/img/contests/w2.jpg',
        '/img/contests/w3.jpg',
        '/img/contests/w4.jpg',
        '/img/contests/w5.jpg',
        '/img/contests/w6.jpg',
        '/img/contests/v1.jpg',
        '/img/contests/v2.jpg',
        '/img/contests/v3.jpg',
        '/img/contests/s1.jpg',
        '/img/contests/s2.jpg',
        '/img/contests/s3.jpg',
      ],
    }
  },
}
</script>

<style scoped lang="scss">
.otstyp__p {
  margin-left: 15px;
}
.ab {
  &__p {
    cursor: pointer;
  }
  &__photos {
    margin: 32px 0;
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 16px;
    max-width: 60vw;
  }
  &__photo {
    width: auto;
    height: 200px;
    margin: auto;
    object-fit: cover;
    cursor: pointer;
    &-vertical {
      width: auto;
      height: 300px;
      margin: auto;
      cursor: pointer;
    }
    &-square {
      width: 350px;
      height: 300px;
      margin: auto;
      cursor: pointer;
    }
  }
}

.ab__video {
  width: 100%;
  margin: 0 auto;
  max-width: 800px; /* Максимальная ширина видео */
  padding: 20px; /* Отступы вокруг видео */
  background-color: #f0f0f0; /* Фоновый цвет */
  border-radius: 10px; /* Закругленные углы */
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); /* Тень */
}

.ab__video video {
  width: 100%; /* Ширина видео */
  height: auto; /* Автоматическая высота */
  border-radius: 10px; /* Закругленные углы */
}

/* Медиа-запросы для адаптивности */

@media (max-width: 768px) {
  .ab__video {
    padding: 10px; /* Уменьшение отступов на меньших экранах */
  }
}

@media (max-width: 480px) {
  .ab__video {
    padding: 5px; /* Ещё меньше отступов на очень маленьких экранах */
  }
}
</style>
