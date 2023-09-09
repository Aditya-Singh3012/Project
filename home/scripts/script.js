//# sourceMappingURL=index.min.js.map
window.onload = function() {
    Particles.init({
        // normal options
        selector: '.background',
        maxParticles: 2000,
        color:'#5b74c9',
        connectParticles: false,
        // options for breakpoints
        responsive: [
          {
            breakpoint: 768,
            options: {
              maxParticles: 10,
              color: '#ffffff',
              connectParticles: false
            }
          }, {
            breakpoint: 425,
            options: {
              maxParticles: 10,
              connectParticles: false
            }
          }, {
            breakpoint: 320,
            options: {
              maxParticles: 0 // disables particles.js
            }
          }
        ]
      });
};