import "../globals.css";

function CoverLogo() {
    return (
        <div className="coverLogo">
            <img src="/cover_logo.svg" alt="Study Association Cover" width="50%" height="auto"/>
        </div>
    );
}

function CareerDayLogo() {
    return (
        <div className="careerDayLogo" style={cDLogoStyle}>
            <img src="/careerday_logo.svg" alt="Cover Career Day"/>
        </div>
    );
}

const cDLogoStyle = {
    padding: '20px',
    width:'50%',
}

export { CoverLogo, CareerDayLogo };