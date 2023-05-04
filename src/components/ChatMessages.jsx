import React, { useState } from 'react';
import ChatMsg from '@mui-treasury/components/chatMsg/ChatMsg';

//const script = ['hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi']

const script = [`I want to build a gazebo, but I’m not sure how to make an informed site selection decision. Could you help me out?`,
`Sure, I can definitely help you with that! Before you build a gazebo, check local laws and zoning regulations to see if you need a building permit.

Site selection is important when building a gazebo. Choose an area that is level or that you can make level. You’ll also need to consider potential obstacles and safety concerns.
Before building any outdoor structure, contact your local utility company to check for underground utility lines. The number 811 is the federally designated "call before you dig" number. It's there to help homeowners and professionals identify where underground lines are buried to avoid damage.
Also be aware of overhead lines. Don’t build your gazebo directly underneath any overhead utility lines.
Consider any trees in the area that might need to be trimmed or removed in the future. It may be better to do that work prior to construction.
If a septic system is present, check the property diagrams for location of the tank and drain field. Do not build over either of these.
If power will be run to the gazebo, check the path between it and the power source to ensure that a wire can be buried.

This information has been retrieved from a how-to guide provided by Home Depot. Please refer to it for your project:
https://www.homedepot.com/c/ah/how-to-build-a-gazebo/9ba683603be9fa5395fab901c5b2f155`,
`I am following this guide now, but frustratingly it does not suggest where I should get the wood for the frame or the shingles for the roof. Suggest some product options for me.`,
`Here is a great wood post that Home Depot carries:
Pressure-Treated Ground Contact Southern Line Timber Wood Post
https://www.homedepot.com/p/6-in-x-6-in-x-16-ft-2-Pressure-Treated-Ground-Contact-Southern-Line-Timber-Wood-Post-261023/100042343
A pressure-treated ground contact Southern Pine timber wood post is a type of wood post that has been treated with chemical preservatives to protect it from decay, insects, and moisture. The term "ground contact" refers to the fact that the wood has been treated to withstand direct contact with the ground, making it ideal for use in outdoor applications where it will be exposed to moisture.

Here are a couple shingle options:
Royal Sovereign Charcoal Algae Resistant 3-Tab Roofing Shingles
https://www.homedepot.com/p/GAF-Royal-Sovereign-Charcoal-Algae-Resistant-3-Tab-Roofing-Shingles-33-33-sq-ft-per-Bundle-26-Pieces-0201180/100040028
Royal Sovereign Charcoal Algae Resistant 3-Tab Roofing Shingles are an asphalt 
shingle made by GAF. They have a dark gray color and a traditional 3-tab design. These shingles are resistant to algae growth, ensuring that your gazebo stays looking clean and attractive. They are also durable, with a strong fiberglass base and a high-quality asphalt coating. These shingles are rated for wind speeds of up to 60 mph and come with a limited lifetime warranty for residential use. Overall, Royal Sovereign Charcoal Algae Resistant 3-Tab Roofing Shingles are a reliable and long-lasting option for your gazebo.

Heritage Rustic Black Architectural Shingles (Average 32.8 sq. ft. Per Bundle)
https://www.homedepot.com/p/Tamko-Heritage-Rustic-Black-Architectural-Shingles-Average-32-8-sq-ft-Per-Bundle-31003625/319064740
These shingles are a classic in the roofing industry, recommended by contractors, builders and homeowners for their quality construction, Limited Lifetime Warranty, beautiful woodshake cut and the best shingle colors available in the market. Heritage shingles have a double-layer fiberglass mat construction with a random-cut sawtooth design. The 2 layers of mat are coated with asphalt, surfaced with mineral granules and then laminated together. They also include a self-sealing strip of asphalt.`
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
