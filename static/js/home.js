document.addEventListener('DOMContentLoaded', function() {

    const homeContent = document.querySelector('.HomeContent');

    homeContent.classList.add('animate');

    function handleAnimation() {

        const isInViewport = (elem) => {
            const bounding = elem.getBoundingClientRect();
            return (
                bounding.top >= 0 &&
                bounding.bottom <= (window.innerHeight || document.documentElement.clientHeight)
            );
        };

        if (isInViewport(homeContent)) {
            homeContent.style.opacity = 1;
            homeContent.style.transform = 'translateY(0)';
        }
    }

    window.addEventListener('scroll', handleAnimation);

    handleAnimation();
});
