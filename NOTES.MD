2/16/2026
- the overal process used by the Session to persist objects
  is known as the unit of work.

- add objects to the Session via add
    ex: Session.add(objName)
-flush: when the session sends the data over to the database
    ex: session.flush()

-identity map:
    -an in-memory store that links all objects
    currently loaded in memory

    - allows comple sets of objects to be manipulated
    without things getting out of sync.
