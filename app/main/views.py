


# Views
@main.route('/', methods=['GET', 'POST'])
def index():
    '''
    View root page function that returns the index page and its data
    '''
    pitch = Pitch.query.filter_by().first()
    title = 'Home'
    businesspitch= Pitch.query.filter_by(category="businesspitch")
    interviewpitch = Pitch.query.filter_by(category="interviewpitch")
    techpitch = Pitch.query.filter_by(category="techpitch")
    pickuppitch = Pitch.query.filter_by(category="pickuppitch")

    # upvotes = Upvote.get_all_upvotes(pitch_id=Pitch.id)

    return render_template('index.html', title=title, pitch=pitch, pickuppitch=pickuppitch,
                           interviewpitch=interviewpitch, businesspitch=businesspitch, techpitch=techpitch)
