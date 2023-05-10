window.addEventListener('load', () => {
    console.log("It's working!")
    const arr = document.querySelector('.swiper')
    console.log(arr)

    const swiper = new Swiper('.swiper', {
        // Optional parameters
        // direction: 'horizontal',
        // loop: true,

        // If we need pagination
        pagination: {
            el: '.swiper-pagination',
        },
        grabCursor: true,
        centeredSlides: true,
        slidesPerView: "auto",
        breakpoints: {
            320: {
                spaceBetween: 30
            },

            768: {
                spaceBetween: 0
            }
        },
        //
        // // Navigation arrows
        // navigation: {
        //     nextEl: '.swiper-button-next',
        //     prevEl: '.swiper-button-prev',
        // },
        //
        // And if we need scrollbar
        scrollbar: {
            el: '.swiper-scrollbar',
        },
    });

    const menu_wrapper = document.querySelector('.menu-wrapper')
    const hamburger_menu = document.querySelector('.hamburger-menu')
    const menu_mobile = document.querySelector('.menu-mobile')
    menu_wrapper.addEventListener('click', function () {
        hamburger_menu.classList.toggle('animate')
        menu_mobile.classList.toggle('show')
    })


    window.onscroll = function() {myFunction()};

    const header = document.querySelector('.header')
    const sticky = header.offsetTop;
    function myFunction() {
        if (window.scrollY > sticky) {
            header.classList.add("sticky");
        } else {
            header.classList.remove("sticky");
        }
    }
})