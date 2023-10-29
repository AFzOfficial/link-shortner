from sqlalchemy.orm import Session

from models.link import Link
from schemas.link import LinkInput
from utils.link import generate_random_string


def get(db: Session, short: str) -> Link | None:
    return db.query(Link).filter(Link.short == short).first()



def create(db: Session, request: LinkInput) -> Link:
    while 1:
        short = generate_random_string()

        if get(db, short):
            continue
        else:
            link = Link(address=request.address, short=short)
            db.add(link)
            db.commit()
            db.refresh(link)
            break

    return link


def update(db: Session, request: LinkInput, short: str) -> Link | None:
    link = get(db, short)

    if link:
        link.address = request.address
        db.commit()
        db.refresh(link)
        return link

    return None


def delete(db: Session, short: str) -> Link | None:
    link = get(db, short)

    if link:
        db.delete(link)
        db.commit()
        return link
    
    return None
