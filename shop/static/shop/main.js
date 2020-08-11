console.log('Hello from stripe');

fetch("/config/")
    .then((result) => { return result.json(); })
    .then((data) => {
      // Initialize Stripe.js
      const stripe = Stripe(data.publicKey);

    document.querySelector("#checkout-button").addEventListener("click", () => {
        // Get Checkout Session ID
        fetch("/checkout-session/")
        .then((result) => { return result.json(); })
        .then((data) => {
          console.log(data);
          // Redirect to Stripe Checkout
          return stripe.redirectToCheckout({sessionId: data.sessionId})
        })
        .then((res) => {
          console.log(res);
        });
      });
    });