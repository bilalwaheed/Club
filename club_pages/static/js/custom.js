<script>
		 $(".anim-slider").animateSlider(
		 	{
		 		autoplay	:true,
		 		interval	:5000,
		 		animations 	:
				{
					0	: 	//Slide No1
					{
						h1	:
						{
							show   	  : "bounceIn",
							hide 	  : "flipOutX",
							delayShow : "delay1s"
	 					},
	 					h2:
	 					{
	 						show 	  : "fadeInUpBig",
							hide 	  : "fadeOutDownBig",
							delayShow : "delay1-5s"
	 					},
	 					h3 	:
	 					{
							show   	  : "bounceInRight",
							hide 	  : "fadeOutRightBig",
							delayShow : "delay1-5s"
	 					},
	 					h4:
	 					{
	 						show 	  : "bounceInUp",
							hide 	  : "fadeOutLeftBig",
							delayShow : "delay2s"
						}
					},
					1	: //Slide No2
					{
						"#todo":
						{
							show 		: "fadeIn",
							hide 		: "fadeOut",
							delayShow   : "delay0-5s"
						},
						"#bounce" 	:
						{
							show 	 	: "bounceIn",
							hide 	 	: "bounceOut",
							delayShow 	: "delay2s"
						},
						"#bounceUp":
						{
							show 	 	: "bounceInDown",
							hide 	 	: "bounceOutLeft",
							delayShow 	: "delay2-5s"
						},
						"#bounceRight":
						{
							show 	 	: "bounceInRight",
							hide 	 	: "bounceOutRight",
							delayShow 	: "delay3s"
						},
						"#fade" :
						{
							show 	 	: "fadeInLeft",
							hide 	 	: "fadeOutLeft",
							delayShow 	: "delay3-5s"
						},
						"#fadeUp":
						{
							show 	 	: "fadeInUpBig",
							hide 	 	: "fadeOutUpBig",
							delayShow 	: "delay4s"
						},
						"#fadeDown":
						{
							show 	 	: "fadeInDownBig",
							hide 	 	: "fadeOutDownBig",
							delayShow 	: "delay4-5s"
						},
						"#rotate" :
						{
							show 	 	: "rotateIn",
							hide 	 	: "rotateOut",
							delayShow 	: "delay5-5s"
						},
						"#rotateRight" :
						{
							show 	 	: "rotateInUpRight",
							hide 	 	: "rotateOutDownRight",
							delayShow 	: "delay6s"
						},
						"#rotateLeft" :
						{
							show 	 	: "rotateInUpLeft",
							hide 	 	: "rotateOutDownLeft",
							delayShow 	: "delay6-5s"
						}
					},
					2	: //Slide No3
					{
						"img#css3"	:
						{
							show 	  : "flipInY",
							hide 	  : "flipOutY",
							delayShow : "delay0-5s"
						},
						"img#html5"	:
						{
							show 	  : "flipInY",
							hide 	  : "flipOutY",
							delayShow : "delay0-5s"
						},
						"img#jquery"  :
						{
							show 	  : "bounceIn",
							hide 	  : "flipOutY",
							delayShow : "delay1-5s"
						},
						"img#modernizr" :
						{
							show 	  : "rollIn",
							hide 	  : "flipOutY",
							delayShow : "delay2s"
						},
						"#animatecss"	:
						{
							show 	  : "lightSpeedIn",
							hide 	  : "flipOutY",
							delayShow : "delay2-5s"
						}
					}
				}
		 	});
		</script>