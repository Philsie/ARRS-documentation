| User         | Password                          | Level    | Status     | Name          |  
|--------------|-----------------------------------|----------|------------|---------------|    
| garlicaxc    | lycanthropexeatpigsx              | observer | Active     | System user   | 

# garlicaxc:lycanthropexeatpigsx

* user<br>
  Login: garlicaxc<br>
  Access level: observer<br>
  Name: System user<br>
  Status: Active<br>

  Description:<br>
  DELETED<br>

  Notes:<br>
  UTF-8<br>

* dir<br>
  * look_for.txt<br>
    `53a9d72a122be8e991028997b05d8658ec81f0cd11c29990`<br>
* notes
  * best<br>
      ```
      https://drive.google.com/drive/u/2/folders/1GNlQnDP7NufYQNck770BJ7phioGtTPb5
      ```
  This contains a file named `blowfish.png`; it's just a picture of a blowfish.
  ```https://stegonline.georgeom.net/image```
  This allowed us to identify a chunk of text embedded in the image. Check the Red 3 bitplane.

  ## What we Know

  Ciphertext: `53a9d72a122be8e991028997b05d8658ec81f0cd11c29990`<br>
  `Blowfish`     - garlicaxc
  `ln;3jn3rfg`   - observer93-5<br>
  `pkcs5padding` - readonly<br>
  `ECB`          - ts0gnar<br>

  This site seems pretty solid: https://www.lddgo.net/en/encrypt/blowfish

  We have a string from observer93-5  which could be a key for the decryption process. We also know the username is presumably `bestwalker`.


