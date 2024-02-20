
'use strict';

$(document).ready(function() {
  const original_price = {{ object.ticket_cost }};
  let price = original_price;
  let attendeeMinCatch = 1;
  let afterTaxPrice = 0;

  const taxes = 0.08;

  const $finalPrice = $('#final_price');
  const $taxes = $('#taxes');
  const $finalPriceInput = $('input[name=final_price_input]');

  const updatePrice = () => {
    // $sevice_f.html((price + 17 ) * .12);
    $taxes.html((price + 17 ) * .12);
    $taxes.html("$" + ((price + 17 ) * .12).toFixed(2));
    $finalPrice.html(price + 17 * (1 + taxes));
    $finalPriceInput.val(price + 17 * (1 + taxes));
  };



  const handleCheckbox = (checkbox, value) => {
    if (checkbox.is(':checked')) {
      price += value;
    } else {
      price -= value;
    }
    updatePrice();
  };

  $('#kcnt-up, #cnt-up').on('click', function() {
    price += original_price;
    attendeeMinCatch++;
    updatePrice();
  });

  $('#kcnt-down, #cnt-down').on('click', function() {
    if (attendeeMinCatch > 1) {
      price -= original_price;
      attendeeMinCatch--;
      updatePrice();
    }
  });

  $('#a-1').on('click', function() {
    handleCheckbox($(this), {{ object.private_room_cost}});
  });

  $('#a-2').on('click', function() {
    handleCheckbox($(this), {{ object.private_guide_costs }});
  });

  $('#a-3').on('click', function() {
    if ($(this).is(':checked')) {
      price -= {{ object.no_lodging_or_transportation_discount }}* attendeeMinCatch;
    } else {
      price += {{object.no_lodging_or_transportation_discount}}* attendeeMinCatch;
    }
    updatePrice();
  });

  updatePrice();
});
