import React from 'react';
import * as jdenticon from 'jdenticon';

export default function Avatar({email}) {
  const svg = jdenticon.toSvg(email, 64);
  return (
    <span dangerouslySetInnerHTML={{__html:svg}} />
  );
}
