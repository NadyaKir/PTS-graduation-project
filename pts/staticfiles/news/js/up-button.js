(function () {
	var topButton = document.querySelector('.top-button');

	window.addEventListener('scroll', function() {
		if (window.pageYOffset >= document.documentElement.clientHeight) {
			topButton.classList.remove('top-button__hidden');
		} 

		if (window.pageYOffset < document.documentElement.clientHeight) {
			topButton.classList.add('top-button__hidden');
		}
	});

	topButton.addEventListener('click', function () {
		window.scrollTo(0, 0);
	});
}());

