import React, { useState } from 'react';
import ChatMsg from '@mui-treasury/components/chatMsg/ChatMsg';

//const script = ['hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi']

const script = [`I want to make a gazebo, but I’m not sure how to go about it. Could you help me out?`,
`Sure, I can definitely help you with that! Building a gazebo can be a fun and rewarding project, and with the right guidance, it can be a relatively simple task. Here are some steps to help you get started:

1. Choose a location: The first step in building a gazebo is to decide where you want to place it. You will need to choose a level area that is free from obstructions and has good drainage. Make sure the location is also accessible from your home or other areas of your property.

2. Design your gazebo: Once you have chosen your location, you will need to design your gazebo. There are many different styles of gazebos, so choose one that fits your needs and your personal taste. You can find gazebo plans online or create your own design.

3. Gather materials: Once you have a design, you will need to gather materials. You will need wood for the frame and roof, concrete footings or blocks, screws, nails, and roofing materials. You may also need tools such as a circular saw, drill, and level.

4. Build the frame: The next step is to build the frame of your gazebo. You will need to cut the wood to the correct lengths and angles according to your design. Use screws and nails to secure the pieces together.

5. Install the roof: Once the frame is complete, you can install the roof. Depending on your design, you may use shingles, tiles, or another roofing material. Make sure the roof is properly installed to ensure it is weatherproof.

6. Finish the gazebo: Finally, you can finish your gazebo with any additional features you desire. You may want to add a railing, seating, or decorative touches.

7. Building a gazebo requires some skill, time, and effort, but it is a great way to enhance the beauty and functionality of your outdoor space. 

Alternatively you could check out this guide provided by the Home Depot site that goes into detail about building a gazebo:

https://www.homedepot.com/c/ah/how-to-build-a-gazebo/9ba683603be9fa5395fab901c5b2f155
`,
`What materials could I use to build the frame and roof?`,
`Here is a great wood post that Home Depot carries:

Pressure-Treated Ground Contact Southern Line Timber Wood Post

https://www.homedepot.com/p/6-in-x-6-in-x-16-ft-2-Pressure-Treated-Ground-Contact-Southern-Line-Timber-Wood-Post-261023/100042343


A pressure-treated ground contact Southern Pine timber wood post is a type of wood post that has been treated with chemical preservatives to protect it from decay, insects, and moisture. The term "ground contact" refers to the fact that the wood has been treated to withstand direct contact with the ground, making it ideal for use in outdoor applications where it will be exposed to moisture.

Here are a few shingle options that Home Depot carries:

1. Royal Sovereign Charcoal Algae Resistant 3-Tab Roofing Shingles
https://www.homedepot.com/p/GAF-Royal-Sovereign-Charcoal-Algae-Resistant-3-Tab-Roofing-Shingles-33-33-sq-ft-per-Bundle-26-Pieces-0201180/100040028

Royal Sovereign Charcoal Algae Resistant 3-Tab Roofing Shingles are an asphalt shingle made by GAF. They have a dark gray color and a traditional 3-tab design. These shingles are resistant to algae growth, ensuring that your gazebo stays looking clean and attractive. They are also durable, with a strong fiberglass base and a high-quality asphalt coating. These shingles are rated for wind speeds of up to 60 mph and come with a limited lifetime warranty for residential use. Overall, Royal Sovereign Charcoal Algae Resistant 3-Tab Roofing Shingles are a reliable and long-lasting option for your gazebo.

2. Heritage Rustic Black Architectural Shingles (Average 32.8 sq. ft. Per Bundle)
https://www.homedepot.com/p/Tamko-Heritage-Rustic-Black-Architectural-Shingles-Average-32-8-sq-ft-Per-Bundle-31003625/319064740
Black architectural shingles are a type of roofing shingle that is designed to resemble the look of traditional slate or cedar shingles. They are typically made of asphalt and are available in a variety of colors, including black.
These shingles are a classic in the roofing industry, recommended by contractors, builders and homeowners for their quality construction, Limited Lifetime Warranty, beautiful woodshake cut and the best shingle colors available in the market. Heritage shingles have a double-layer fiberglass mat construction with a random-cut sawtooth design. The 2 layers of mat are coated with asphalt, surfaced with mineral granules and then laminated together. They also include a self-sealing strip of asphalt.
`
]

const ChatMessages = ({currMessage}) => {
  return (<div style={{height: '95%', whiteSpace: 'pre-line'}}>
    {
      script.slice(0, currMessage).map((message, index) => (
      <ChatMsg
        side={!(index % 2) ? 'right' : 'left'}
        avatar={''}
        messages={[message]}
      />))
    }
  </div>)
}

export default ChatMessages;